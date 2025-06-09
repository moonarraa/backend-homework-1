# Beauty Appointment Assistant

A simple full-stack app for booking beauty appointments. Features a FastAPI backend with CRUD operations and a React frontend widget that fetches data from the backend.

---

## 🥉 Basic Level Features

- **CRUD operations** for Users, Masters, Procedures, and Appointments (FastAPI backend)
- **Frontend (React widget)** fetches and displays salon data from the backend

---

## Quick Start

### Backend
1. Install dependencies:
   ```sh
   cd backend
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   uvicorn src.main:app --reload
   ```
2. The backend runs on `http://localhost:8000` by default.

### Frontend
1. Install dependencies and start:
   ```sh
   cd frontend
   npm install
   npm start
   ```
2. The React widget will fetch salon data from the backend.

---

## API Example
- `GET /api/salons/hair` — Get list of salons

---

