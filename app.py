import streamlit as st
import os
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
import json

# ✅ Set page config
st.set_page_config(page_title="Google Sheet Cleaner", layout="wide")

# ✅ Download ZIP button (if available)
if os.path.exists("google-sheet-cleaner.zip"):
    with open("google-sheet-cleaner.zip", "rb") as zip_file:
        zip_bytes = zip_file.read()
    st.download_button(
        label="📦 Download Full Source Code (ZIP)",
        data=zip_bytes,
        file_name="google-sheet-cleaner.zip",
        mime="application/zip"
    )
else:
    st.warning("⚠️ ZIP file not found. Please make sure 'google-sheet-cleaner.zip' exists.")

# ✅ Title and subtext
st.title("🧹 Google Sheet Cleaner - AppSumo Edition")
st.write("Clean messy Google Sheet data with 1 click — no setup required!")

# ✅ Sidebar - How to Use
with st.sidebar:
    st.header("🔧 How to Use")
    st.markdown("""
    1. Go to [Google Console](https://console.cloud.google.com/)
    2. Create a Service Account and download the JSON key
    3. Share your Google Sheet with the **client_email** from JSON
    4. Paste the Sheet URL and name below
    """)
    demo_mode = st.checkbox("Use Demo Sheet")

# ✅ User Inputs
if demo_mode:
    sheet_url = "https://docs.google.com/spreadsheets/d/1PKkDemoSheetURL/edit"
    sheet_name = "Sheet1"
    creds_file = None
else:
    sheet_url = st.text_input("📄 Google Sheet URL")
    sheet_name = st.text_input("📑 Sheet Name (e.g. Sheet1)")
    creds_file = st.file_uploader("🔐 Upload Google Service Account JSON", type=["json"])

# ✅ Authenticate Google Sheets
def authenticate(creds_dict):
    scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    creds = Credentials.from_service_account_info(creds_dict, scopes=scopes)
    client = gspread.authorize(creds)
    return client

# ✅ Fetch data from sheet
def fetch_data(client, sheet_url, worksheet_name):
    sheet = client.open_by_url(sheet_url)
    worksheet = sheet.worksheet(worksheet_name)
    return pd.DataFrame(worksheet.get_all_records())

# ✅ Clean the DataFrame
def clean_dataframe(df):
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.title()
    df.replace(r'^\s*$', pd.NA, regex=True, inplace=True)

    # Clean emails
    if 'Email' in df.columns:
        df['Email'] = df['Email'].str.strip().str.lower()
        df['Email'] = df['Email'].str.replace(r'\.\.+', '.', regex=True)
        df['Email'] = df['Email'].str.replace(r'@+', '@', regex=True)
        df['Email'] = df['Email'].str.replace(r'\.con$', '.com', regex=True)
        df['Email'] = df['Email'].str.replace(r'(@.*)@', r'\1', regex=True)

    # Drop rows with empty name/email or invalid emails
    if 'Name' in df.columns and 'Email' in df.columns:
        df = df[df['Name'].notna() & df['Email'].notna()]
        df = df[df['Email'].str.contains(r'^[^@]+@[^@]+\.[^@]+$', na=False)]

    # Clean phone numbers
    phone_cols = [col for col in df.columns if any(x in col.lower() for x in ['phone', 'mobile', 'contact'])]
    for col in phone_cols:
        df[col] = df[col].astype(str).str.replace(r'\D', '', regex=True)
        df = df[df[col].str.match(r'^\d{6,}$')]

    # Drop duplicate emails
    if 'Email' in df.columns:
        df = df.drop_duplicates(subset='Email')
    df = df.drop_duplicates()

    # Fill missing values
    for col in df.columns:
        if df[col].dtype in ['float64', 'int64']:
            df[col].fillna(df[col].median(), inplace=True)
        elif df[col].dtype == 'object' and df[col].isnull().any():
            df[col].fillna(df[col].mode()[0], inplace=True)

    return df

# ✅ Convert to CSV
def to_csv_bytes(df):
    return df.to_csv(index=False).encode("utf-8")

# ✅ Main Button - Clean Sheet
if st.button("🚀 Clean My Sheet"):
    try:
        if demo_mode:
            creds_dict = json.loads(st.secrets["demo_credentials"])
        elif not sheet_url or not sheet_name or not creds_file:
            st.error("❌ Please provide Sheet URL, name, and upload credentials.")
            st.stop()
        else:
            creds_dict = json.loads(creds_file.read())

        client = authenticate(creds_dict)
        df_raw = fetch_data(client, sheet_url, sheet_name)
        df_clean = clean_dataframe(df_raw)

        st.success("✅ Sheet cleaned successfully!")
        st.dataframe(df_clean)

        st.download_button(
            label="📥 Download Cleaned CSV",
            data=to_csv_bytes(df_clean),
            file_name="cleaned_sheet.csv",
            mime="text/csv"
        )

    except Exception as e:
        st.error(f"❌ Error: {e}")
