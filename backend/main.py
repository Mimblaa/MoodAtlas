from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

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

@app.get("/")
def read_root():
    return {"message": "MoodAtlas backend is running."}

@app.post("/analyze")
def analyze_mood(entry: MoodEntry):
    # Dummy placeholder
    return {
        "emotion": "calm",
        "confidence": 0.85
    }
