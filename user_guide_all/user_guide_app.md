# 🚀 How to Use `app.py` – Your Google Sheets Data Cleaner 🧹

Welcome! This script is your **automated assistant** for cleaning messy Google Sheets — even if you don’t know how to code! 🤖✨

---

## ✅ What Is `app.py`?

This is the **main script** that does all the magic. When you run it, it will:

- Connect to your Google Sheet ✅  
- Read your raw data 📄  
- Clean & fix messy data (emails, missing values, duplicates, etc.) 🧼  
- Save the cleaned version in a new tab called `CleanedData` 📊

You just need to run it — and it will take care of everything!

---

## 🛠️ How to Run `app.py`

### 🟢 Option 1: EASIEST – Just double-click `run.bat` (Windows only)

If you're on Windows:

1. Make sure you're in the folder that has:
    - `app.py`
    - `run.bat`
    - `credentials.json`
    - `requirements.txt`
2. ✅ Double-click `run.bat`  
It will automatically run `app.py` in the background and clean your data!

---

### 🟡 Option 2: Manual Method (Using Command Prompt)

If you're not using `run.bat`, follow these simple steps:

#### Step 1: Open Command Prompt (CMD)

- Press **Start** → Type `cmd` → Hit **Enter**

#### Step 2: Go to the Project Folder

Type this in CMD to go to the folder where `app.py` is located:

```bash
cd path_to_your_folder
```

Example:

```bash
cd C:\Users\JohnDoe\Downloads\GoogleSheetsDataCleaner
```

#### Step 3: Run the Script

Type this and hit **Enter**:

```bash
python app.py
```

Wait a few seconds... and your data will be cleaned and saved inside your Google Sheet! 🧠📊

---

## 🔍 What Does It Clean?

Here’s what happens automatically:

- ✅ Cleans column names (lowercase, removes spaces)
- ✅ Converts empty cells to NaN (for better processing)
- ✅ Validates email format (removes invalid ones)
- ✅ Removes rows with missing name/email
- ✅ Removes duplicate rows
- ✅ Fills missing numbers with **median**
- ✅ Fills missing text with **most frequent value (mode)**
- ✅ Saves the clean version to a new tab: `CleanedData`

---

## ⚠️ Facing Errors?

If something goes wrong, check these:

- ❓ Is your `credentials.json` file correctly downloaded and placed?
- ❓ Did you **share your Google Sheet** with the service account email?
- ❓ Is your **Google Sheet ID** correctly set in the code?

👉 Refer to:
- `user_guide_json.md` – for setting up credentials  
- `user_guide_runbat.md` – for help with `run.bat`

---

## 🎉 Done!

You now have a fully working, auto-cleaning Google Sheets tool — powered by Python, but designed for **non-tech users like you** 💪✨

Happy Automating! 🧠💼
