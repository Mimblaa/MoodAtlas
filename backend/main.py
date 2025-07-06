import logging
import datetime
import os
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from transformers import pipeline
from langdetect import detect
from googletrans import Translator
from db import SessionLocal, User, MoodEntryDB, EmotionAnalysis
from dotenv import load_dotenv



PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
load_dotenv(dotenv_path=os.path.join(PROJECT_ROOT, '.env'))
FRONTEND_ORIGINS = os.getenv("FRONTEND_ORIGINS", "http://localhost:3000").split(",")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=FRONTEND_ORIGINS,  # Configurable frontend origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserCreate(BaseModel):
    username: str

class UserOut(BaseModel):
    id: int
    username: str
    class Config:
        orm_mode = True

class MoodEntry(BaseModel):
    content: str
    user_id: int | None = None

class MoodEntryInDB(BaseModel):
    id: int
    user_id: int | None
    entry_text: str
    entry_date: datetime.date
    created_at: datetime.datetime
    class Config:
        orm_mode = True

emotion_classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    return_all_scores=True
)
translator = Translator()

# --- API endpoints ---
@app.get("/")
def read_root():
    return {"message": "MoodAtlas backend is running."}


# --- User endpoints ---
@app.get("/users", response_model=list[UserOut])
def get_users():
    db = SessionLocal()
    try:
        users = db.query(User).all()
        return users
    finally:
        db.close()

@app.post("/users", response_model=UserOut)
def create_user(user: UserCreate):
    db = SessionLocal()
    try:
        new_user = User(username=user.username)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    finally:
        db.close()

# --- Mood analysis endpoint ---
@app.post("/analyze")
def analyze_mood(entry: MoodEntry):
    text = entry.content
    user_id = entry.user_id
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
    # Save entry and analysis to DB
    db = SessionLocal()
    try:
        mood_entry = MoodEntryDB(
            user_id=user_id,
            entry_text=entry.content,
            entry_date=datetime.date.today()
        )
        db.add(mood_entry)
        db.commit()
        db.refresh(mood_entry)
        analysis = EmotionAnalysis(
            mood_entry_id=mood_entry.id,
            emotion_label=best['label'],
            emotion_score=float(best['score']),
            sentiment=None
        )
        db.add(analysis)
        db.commit()
        db.refresh(analysis)
    finally:
        db.close()
    return {
        "emotion": best['label'],
        "confidence": round(float(best['score']), 2),
        "lang": lang
    }
