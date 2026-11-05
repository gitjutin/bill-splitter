# Itemized

Split bills or receipts with a group of people by snapping a photo of the receipt, and allowing the app to split the cost.

> CURRENTLY: Work in progress!

## Features 
- [X] Evenly split the bill
- [ ] Manual entry ( split by item w/ names for individuals)
- [ ] History page ( track previous bills )
- [ ] Receipt scanning ( computer vision specifically Optical Character Recognition )
- [ ] Choose a picture from gallery ( split a bill that was photographed at a different time )

## Tech Stack
Python, FastAPI, Pytest, Flutter, PostgreSQL (planned), AWS (planned)

## First-time setup
```bash
cd bill-splitter/backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Running the backend
```bash
cd backend
venv\Scripts\activate
fastapi dev app/main.py
```
