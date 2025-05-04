# CMR Faculty Schedule App

A Flask web application to display and search faculty schedules for CMR Technical Campus.

## Features
- View a list of faculty members with their IDs and phone numbers.
- Search faculty schedules by ID, day, and period.

## Project Structure
- `app.py`: Main Flask application.
- `faculty_schedule.csv`: Data file with faculty schedules.
- `static/logo.png`: Logo for CMR Technical Campus.
- `templates/`: HTML templates (`index.html`, `search.html`).

## Deployment
1. Push the code to a GitHub repository.
2. Deploy on Render:
   - Environment: Python 3
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`

## Dependencies
See `requirements.txt` for a full list:
- Flask
- pandas
- gunicorn
