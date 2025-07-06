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
```

### 2. Prerequisites

Make sure you have installed:
- **Python 3.8+** ([download here](https://www.python.org/downloads/))
- **Node.js 16+** ([download here](https://nodejs.org/))
- **npm** (automatically installed with Node.js)

### 3. Running Backend (FastAPI)

```bash
# Navigate to backend directory
cd backend

# Create Python virtual environment (optional but recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start backend server
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Backend will be available at: **http://localhost:8000**

### 4. Running Frontend (React)

Open a **new terminal** and run:

```bash
# Navigate to frontend directory
cd frontend

# Install npm dependencies
npm install

# Start React application
npm start
```

Frontend will be available at: **http://localhost:3000**

### 5. You're Ready! 🎉

After starting both servers:
1. Open your browser and go to **http://localhost:3000**
2. Backend API will be automatically available for the frontend
3. API Documentation: **http://localhost:8000/docs**

---

## 🔧 Troubleshooting

### CORS Issues
If you see CORS errors, make sure that:
- Backend is running on port 8000
- Frontend is running on port 3000
- Both servers are running


### AI Model Issues
On first run, the application will download the HuggingFace model (~500MB). Make sure you have an internet connection.

---

## 📁 Project Structure

```
MoodAtlas/
├── backend/          # FastAPI backend
│   ├── main.py       # Main application file
│   └── requirements.txt
├── frontend/         # React frontend
│   ├── src/
│   │   ├── App.js    # Main component
│   │   └── ...
│   └── package.json
└── README.md
```
