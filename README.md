# 🌌 MoodAtlas – Interactive Emotion Mapping App (Offline, AI-powered)

**MoodAtlas** is a local web application that helps users explore and understand their emotional patterns using an interactive visual map. By entering short daily mood reflections, the app uses an AI model to analyze emotions and position them on a dynamic emotion landscape.

This project is designed for **full local usage**, with **no external API calls**, ensuring **maximum privacy** and ownership of your personal data.

---

## 🧠 Features

- 📝 Write daily mood entries (free text)
- 🤖 Local AI analyzes emotional tone and sentiment
- 🗺️ Visual "emotion map" places moods in emotional space
- 📈 View history and trends through a dynamic chart
- 🛡️ All data is stored locally (MariaDB) – 100% private
- ⚙️ Built with **React**, **FastAPI**, and **MariaDB**

---

## 🧰 Tech Stack

| Layer       | Technology            |
|-------------|------------------------|
| Frontend    | React, Axios, Chart.js |
| Backend     | FastAPI (Python)       |
| Database    | MariaDB (SQLAlchemy ORM) |
| AI/NLP      | HuggingFace Transformers (local)/ OpenAI |
| Optional    | Docker (for setup), Framer Motion (for map animation) |

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/moodatlas.git
cd moodatlas
