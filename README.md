# 🧼 Google Sheets Data Cleaner – One-Click Automation with Python

Effortlessly clean messy data in Google Sheets using this beginner-friendly Python tool — no coding required.

This automation script helps you clean names, emails, missing values, and duplicates in **just one click**.  
Designed especially for **marketers, HRs, analysts, freelancers**, and anyone tired of cleaning spreadsheets manually.

---

## ✅ What This Tool Does (Smart Data Cleaning Logic)

| Step                                         | Description                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| Clean Column Names        | Converts headers to lowercase, removes extra spaces                        |
| Convert Blanks to NaN     | Standardizes all empty cells                                                |
| Remove Invalid Emails     | Keeps only properly formatted email addresses                              |
| Drop Incomplete Rows      | Removes rows missing essential info like name or email                     |
| Remove Duplicates         | Keeps your dataset clean and unique                                         |
| Fill Missing Numbers      | Replaces with median values                                                 |
| Fill Missing Text         | Fills with the most common value (mode)                                     |
| Save to `CleanedData` Tab | Your cleaned dataset appears in a new tab without changing the original     |

---

## 📁 Folder & File Structure

```
📦 GoogleSheetsDataCleaner/
├── app.py                   # Main script (Python automation)
├── run.bat                  # One-click runner for Windows users
├── requirements.txt         # List of required Python libraries
├── credentials_sample.json  # Sample credentials file (DO NOT USE - for reference only)
├── README.md                # This documentation

# Guides for different user levels
├── for_non_technical_users/
│   ├── user_guide_app.md
│   ├── user_guide_runbat.md
│   ├── user_guide_requirements.md
│   └── user_guide_json.md

├── for_technical_users/     # Optional - extra tips for developers
```

---

## 🚀 Quick Start Guide

### 🔧 Step 1: Install Python (Only Once)

Download and install from: https://www.python.org/downloads/  
✅ Make sure to check **“Add Python to PATH”** during install.

To verify:
```bash
python --version
```

---

### 📦 Step 2: Install Required Libraries

Run this in Command Prompt (inside the folder):

```bash
pip install -r requirements.txt
```

---

### 🔐 Step 3: Set Up Google Sheets API

> This allows the script to access and clean your Google Sheets data securely.

#### 1. Create a Google Cloud Project  
#### 2. Enable:
- Google Sheets API  
- Google Drive API

#### 3. Create a Service Account  
- Download the credentials as `.json`  
- Rename it to: `credentials.json`  
- Save it in the **main folder** (same place as `app.py`)

👉 See `for_non_technical_users/user_guide_json.md` for detailed steps with screenshots.

---

### 📄 Step 4: Share Your Sheet

- Open your Google Sheet  
- Click **Share**  
- Paste the service account email from `credentials.json`  
- Give **Editor** access  

✅ Done! The script can now clean your sheet.

---

## ▶️ How to Run

### 🖱️ Non-Technical Users (Windows)

Just double-click:
```
run.bat
```

It will launch the script and clean your data in seconds!

---

### 💻 Technical Users

You can also run manually:
```bash
python app.py
```

---

## 🔐 Security Notice

**Never share your `credentials.json` publicly.**  
It contains sensitive API keys. We include only a sample file for format reference.

---

## 📍 Example Use Cases

- 🧑‍💼 Recruiters cleaning messy resumes and contact lists  
- 📊 Analysts preparing consistent datasets  
- 🛍️ E-commerce owners handling messy order sheets  
- 📧 Marketers cleaning up email campaigns lists  
- 💼 Freelancers working with client data regularly

---

## 🛠️ Customization

Want to:
- Clean other columns?
- Add new cleaning logic?
- Export to Google Drive?

👉 This script is fully open-source.  
If you’re a developer, feel free to modify `app.py` as needed!

---

## 🧠 Bonus: Why This is a Game-Changer

Traditional spreadsheet cleaning = hours of dragging, filtering, fixing...  
With this tool → You do it all **in one click**, with 100% consistency.

---

## 📞 Support & Feedback

Have a question or want a custom version?  
📩 Email: `mdhasanurrahman138@gmail.com`  
Or open an issue on GitHub.

---

## 🙌 Built For You

Whether you're a busy marketer, startup founder, or HR exec — this tool was built to save your time and sanity.

**Start automating today!**
