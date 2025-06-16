from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from transformers import pipeline
from langdetect import detect
from googletrans import Translator
import logging


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adres frontendu
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class MoodEntry(BaseModel):
    content: str

emotion_classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)
translator = Translator()

@app.get("/")
def read_root():
    return {"message": "MoodAtlas backend is running."}

@app.post("/analyze")
def analyze_mood(entry: MoodEntry):
    text = entry.content

    # Detect language and translate to English for better emotion analysis
    try:
        lang = detect(text)
    except Exception:
        lang = "en"
    if lang != "en":
        try:
            translated = translator.translate(text, src=lang, dest="en")
            text = translated.text
        except Exception as e:
            logging.error(f"Translation failed: {e}")
            pass  # fallback: use original text if translation fails
    results = emotion_classifier(text)[0]
    best = max(results, key=lambda x: x['score'])
    return {
        "emotion": best['label'],
        "confidence": round(float(best['score']), 2),
        "lang": lang
    }
