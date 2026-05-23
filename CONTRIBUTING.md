# Contributing

Thank you for helping improve this OpenCV and MediaPipe demo collection.

## Setup

1. Create and activate a Python virtual environment:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

2. Install required packages:

```powershell
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

## Validation

Run the project validation script before adding or updating demos:

```powershell
python scripts\validate_project.py
```

The validation script checks for syntax issues and unsafe file names.

## File naming

Use snake_case for Python demo filenames and avoid spaces. This keeps scripts easy to run from the command line.

## Documentation

Update `README.md` whenever you add or rename demos.
