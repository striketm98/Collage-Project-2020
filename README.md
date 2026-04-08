# E-Tricycle Portal

A cleaned-up, chatbot-style upgrade of the original E-Tricycle registration project.

## What it does

- Chat-style register and login flow
- Saves vehicle records to `E-tricycle.xlsx`
- Validates contact numbers and email addresses
- Prevents duplicate vehicle registration numbers
- Shows helpline details inside the app
- Uses a cleaner, more maintainable code structure

## Project Files

- `College.py` - main application entry point
- `E-tricycle.xlsx` - Excel workbook used as the local data store
- `Poject101/E-tricycle/index.html` and `style.css` - older web mockup files kept in the repo

## Requirements

- Python 3.10 or newer
- `openpyxl`

Install the dependency:

```bash
pip install openpyxl
```

## Run the App

From the project folder:

```bash
python College.py
```

## How to Use

1. Open the app.
2. Click `Register` and answer the chatbot prompts one by one.
3. Use `Login` to verify an existing vehicle registration number and security key.
4. Click `Helpline` if you need the support contact details.
5. Use `Reset Chat` to start over.

## Data Storage

The app stores registrations in the workbook next to the script. If the workbook does not exist, the app creates it automatically with the required headers.

## Notes

- This version is designed to be easier to extend with more AI-friendly features later.
- The UI is still lightweight and fully local, so no internet connection is required to use the app.

