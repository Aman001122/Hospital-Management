# Hospital Appointment & Queue Management System

Simple CLI app to register patients, generate doctor-wise tokens, maintain queues, search and export daily summary.

## Files
- main.py
- db.py
- models.py
- utils.py
- schema.sql

## Requirements
- Python 3.8+
- No external packages required

## Setup & Run
1. Create project folder and put files inside.
2. Open terminal in project folder.
3. (optional) create virtualenv:
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
4. Run:
   python main.py

## Usage
- Choose menu options to register patients, call next patient, search by name/token, and export reports.
- Daily report export writes `daily_report.txt` and `patients_export.json`.

## Notes
- Database file `hospital.db` will be created in project folder.
