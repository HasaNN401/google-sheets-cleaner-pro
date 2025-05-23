# 👨‍💻 Python + VS Code Setup Guide (for Technical Users)

This guide will walk you through setting up the environment to run the **Google Sheets Data Cleaning Automation Script** using Python and Visual Studio Code (VS Code).

---

## ⚙️ Step 1: Install VS Code

🔗 [Download VS Code](https://code.visualstudio.com/)

✅ During installation, make sure to check:

- ✔️ Add to PATH  
- ✔️ Register Code as editor

Open VS Code after installation.

---

## 🐍 Step 2: Install Python

🔗 [Download Python](https://www.python.org/downloads/)

✅ Recommended: Python 3.8 or above  
During installation, be sure to check:

- ✔️ Add Python to PATH

To verify installation, open Terminal/Command Prompt and run:

```bash
python --version
```

You should see something like `Python 3.11.0`

---

## 📂 Step 3: Clone or Open Project Folder

Make sure your working directory contains:

```
app.py
run.bat
credentials.json
requirements.txt
```

You can open the entire folder in VS Code.

---

## 📦 Step 4: Install Required Libraries

Run this in your Terminal or VS Code terminal:

```bash
pip install -r requirements.txt
```

This will install:

- `pandas`
- `gspread`
- `oauth2client`
- `schedule`

---

## 🔑 Step 5: Google Sheets API Setup

1. Go to: https://console.cloud.google.com/
2. Create a new project.
3. Enable these APIs:
   - ✅ Google Sheets API
   - ✅ Google Drive API
4. Create a **Service Account** under IAM & Admin
5. Give it **Editor** role
6. Generate a **JSON key** and save it as `credentials.json` in your project folder

---

## 📤 Step 6: Share Your Google Sheet

Open your Google Sheet and click **Share**  
Copy the `client_email` from `credentials.json` and paste it in the Share dialog  
Give it **Editor** access.

---

## ▶️ Step 7: Run the Script

You can run it manually via:

```bash
python app.py
```

Or for convenience on Windows, just **double-click `run.bat`**.

---

## ✅ Output

- Input Tab: `RawData`  
- Cleaned Output: `CleanedData` (new tab will be created)

---

## 🧹 What the Script Does:

- Cleans column names
- Converts blanks to NaN
- Drops invalid emails or missing names
- Removes duplicates
- Fills missing values
- Saves clean data to a new tab

---

🎉 You’re all set!  
Happy automating and customizing!
