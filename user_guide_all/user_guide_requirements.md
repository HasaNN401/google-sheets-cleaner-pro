# 📦 Required Libraries to Run the Script – `requirements.txt` Guide 🧠

Before your data cleaning script can run, Python needs some **special tools (libraries)** to talk to Google Sheets and clean data smartly.  
This file `requirements.txt` helps you install everything in one go! ✅

---

## 🧰 What Is `requirements.txt`?

It’s a **list of all the Python libraries** needed for this script to work properly.

Libraries listed inside:
```
gspread         # Connects to Google Sheets
oauth2client    # Authenticates with Google
pandas          # Handles and cleans your data
schedule        # (Optional) For scheduling tasks
```

---

## 🟢 How to Install Everything (Step-by-Step)

> You’ll do this only once — like setting up your toolbox! 🧰

### ✅ Step 1: Open Terminal / Command Prompt

On Windows:
- Press `Win + R`, type `cmd`, and press Enter

Or

- Open the folder where your script is
- Hold `Shift + Right Click` → Choose **"Open PowerShell window here"**

---

### ✅ Step 2: Run This Command

Copy and paste this line 👇 and hit Enter:

```
pip install -r requirements.txt
```

⏳ Wait a few seconds… Python will install all needed libraries automatically.

You’ll see messages like:
```
Successfully installed pandas gspread oauth2client schedule
```

---

## 💡 Tip: Install One by One (If Needed)

If the above doesn’t work, you can install each manually:

```
pip install pandas
pip install gspread
pip install oauth2client
pip install schedule
```

---

## 🚫 Common Errors & Fixes

| Problem ❌                                 | Solution 💡                          |
|----------------------------------|--------------------------------------|
| `pip` not recognized             | Python isn’t added to PATH. Reinstall Python and check ✅ "Add to PATH" |
| Slow install or timeout          | Try again with internet connection 🔁 |
| Access denied                     | Try opening CMD as Administrator     |

---

## ✅ You're Done!

Once these are installed, you don’t need to do it again.  
Your script is now ready to talk to Google Sheets and clean data like a pro! 🚀📊

---

> 🧠 Bonus: You can open and edit `requirements.txt` in any text editor if you ever want to add more tools.
