# Flask App — Simple SQLite Guestbook

A lightweight Flask web app that stores and displays guestbook entries using a local SQLite database.  
Built to demonstrate Flask fundamentals, MVC-style structure, and Dockerized deployment.

---

## Features

- 📝 Add and view guestbook entries  
- 💾 Uses SQLite (`entries.db`) for easy local storage  
- 🧩 Clean MVC-style organization (models, routes, templates)  
- 🐳 Docker-ready with both small and large image options  
- 📸 Includes screenshots (`screenshots.pdf`) for quick preview  

---

## 🗂️ Project Structure
```
├── gbmodel/ # Model layer for database access
├── static/ # Static assets (CSS, JS, images)
├── templates/ # HTML templates (Jinja2)
├── app.py # Main Flask application (routes/controllers)
├── index.py # Helper / entry script
├── insert.py # Inserts sample entries
├── entries.db # SQLite database (auto-created)
├── requirements.txt # Python dependencies
├── Dockerfile.small # Lightweight Docker build
├── Dockerfile.large # Full-featured Docker build
└── screenshots.pdf # Example UI screenshots
```

---

## Setup & Run (Local)

### 1️⃣ Create a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate       # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
