# 🧑‍💻 Windows Guide (Non-Technical Users) – Run Google Sheets Cleaner Easily!

Hi there! 👋  
Even if you’ve **never coded before**, don’t worry! This guide will help you run your data cleaning tool in just a few simple steps — just follow along like a checklist ✅

---

## 📦 Step 1: Double Click to Start (The Easy Way)

Just find the file called:

```
run.bat
```

🖱️ **Double click** on it.

It will automatically:
- Open the script
- Clean your data from the sheet
- Save the cleaned version in the `CleanedData` tab

✅ **That’s it! You don’t need to type anything.**

---

## 📝 Before Running the Script (Do This One-Time Setup)

### 1.Make sure these 4 files are in the same folder:
```
✅ app.py  
✅ run.bat  
✅ credentials.json  
✅ requirements_installed.txt (you'll get this after setup)
```

### 2️.Make sure your Google Sheet:
- Has a tab named `RawData` (this is where you put your messy data)
- The script will create a new tab called `CleanedData` — don’t worry, it will happen automatically!

### 3️.Your Google Sheet must be shared with a special email
- Open `credentials.json`
- Copy the email written next to `"client_email"`
- Go to your Google Sheet → click **Share** → paste that email → give **Editor** access

---

## 🧪 Need Help Installing Everything? (One-Time Setup)

If you haven't done the first-time setup (installing Python, VS Code, and libraries), ask someone technical or follow the detailed guide in:

```
📁 for_non_technical_users/
   └── windows_user_guide.md (this file!)
```

Or ask someone to help you set it up once — after that, you’ll never need to touch it again!

---

## 🎉 You’re Done!

From now on, anytime you want to clean data:

➡️ Just double-click on `run.bat`  
💡 The cleaned data will appear in your Google Sheet under the `CleanedData` tab  
🧹 Messy data becomes clean in seconds — no tech knowledge needed!

---

👍 If you face any issue, ask your support person or check the full guide folder.

Have fun automating! 🎯🚀
