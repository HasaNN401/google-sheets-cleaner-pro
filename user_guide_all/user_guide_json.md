# 📋 user_guide_json.md

# How to Set Up Your `credentials.json` for Google Sheets API

To allow your Python script to access and edit your Google Sheets, you need a special JSON file called `credentials.json`. This file contains your Google Cloud service account details securely.

---

## Step-by-Step Guide to Get `credentials.json`

1. **Create a Project in Google Cloud Console**  
   - Visit: https://console.cloud.google.com/  
   - Login with your Google account  
   - Click **Select Project** → **New Project**  
   - Give your project a name (e.g., `google-sheets-automation`)  
   - Click **Create**

2. **Enable APIs**  
   - Inside your project dashboard, go to **APIs & Services** → **Library**  
   - Search and enable:  
     - **Google Sheets API**  
     - **Google Drive API**

3. **Create a Service Account**  
   - Go to **IAM & Admin** → **Service Accounts**  
   - Click **Create Service Account**  
   - Name it (e.g., `gsheets-automation`)  
   - Assign Role → **Project** → **Editor**  
   - Click **Done**

4. **Generate the JSON Key File**  
   - Click on the created service account  
   - Go to **Keys** tab → **Add Key** → **Create New Key**  
   - Choose **JSON** and download the file  
   - Save this file as `credentials.json` in your project folder  
   - **Keep this file safe and do not share publicly!**

5. **Share Your Google Sheet with the Service Account**  
   - Open your Google Sheet in the browser  
   - Click **Share**  
   - Open the `credentials.json` file in a text editor  
   - Copy the email address under `"client_email"` (looks like `xxxx@xxxx.iam.gserviceaccount.com`)  
   - Paste this email into the Share box of your Google Sheet and give it **Editor** access  
   - Click **Send**

---

## Important Notes

- The `credentials.json` file is your key to allowing the script to access Google Sheets  
- Never upload or expose this file publicly or in repositories without protection  
- If you lose this file, you can generate a new one anytime from Google Cloud Console  

---

✅ Now you are ready to use the `credentials.json` file to authenticate your Python script with Google Sheets API!

Happy automating! 🚀
