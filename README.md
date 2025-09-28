# SmartEdu

## Overview
SmartEdu is an interactive educational platform built with Django and Django Channels. It supports quizzes, real-time multiplayer challenges, leaderboards, notes, and an AI chatbot.

## Prerequisites
- Python 3.11+
- PostgreSQL (or SQLite fallback)
- Redis (for Channels)

## Setup
1. Clone the repo
2. Create and activate a virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Set environment variables (see `.env.example`)
5. Run migrations: `python manage.py migrate`
6. Create superuser: `python manage.py createsuperuser`
7. Run development server: `python manage.py runserver`
8. Run Channels server with Daphne if needed: `daphne smartedu.asgi:application`

## Deployment
- Use Docker or deploy on platforms like Heroku, Render, or PythonAnywhere
- Configure environment variables accordingly
- Use Redis for channel layers in production
- Collect static files: `python manage.py collectstatic`

## Usage
- Register as student or teacher
- Create and take quizzes
- Participate in real-time multiplayer challenges
- View leaderboards
- Upload and manage notes (teachers)
- Chat with AI chatbot for help

## Contribution
Feel free to fork, create issues, and send pull requests!

## License
MIT License
