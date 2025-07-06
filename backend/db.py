import os
import datetime
from sqlalchemy import create_engine, Column, Integer, String, Text, Date, ForeignKey, Float, TIMESTAMP
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from dotenv import load_dotenv


load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)
    entries = relationship("MoodEntryDB", back_populates="user")

class MoodEntryDB(Base):
    __tablename__ = "mood_entries"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    entry_text = Column(Text, nullable=False)
    entry_date = Column(Date, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)
    user = relationship("User", back_populates="entries")
    analysis = relationship("EmotionAnalysis", back_populates="mood_entry", uselist=False)

class EmotionAnalysis(Base):
    __tablename__ = "emotion_analysis"
    id = Column(Integer, primary_key=True, index=True)
    mood_entry_id = Column(Integer, ForeignKey("mood_entries.id"), nullable=False)
    emotion_label = Column(String(50), nullable=False)
    emotion_score = Column(Float)
    sentiment = Column(String(20))
    mood_entry = relationship("MoodEntryDB", back_populates="analysis")

Base.metadata.create_all(bind=engine)
