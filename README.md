# Agri Web (Minimal Flask site)

This is a small Flask website with pages: Home, Products, Product Detail, About, and Contact.

Getting started (PowerShell on Windows):

1. Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies

```powershell
pip install -r requirements.txt
```

3. Run the app

```powershell
python app.py
```

Open http://127.0.0.1:5000 in your browser.

Troubleshooting:
- If executing Activate.ps1 is blocked, run `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` in an elevated PowerShell.
- If Flask import fails, ensure the venv is activated and `pip install -r requirements.txt` completed successfully.
