@echo off
cd /d %~dp0

echo ---------------------------------------------
echo  🔍 Checking Python installation...
echo ---------------------------------------------
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo ❌ Python is not installed or not added to PATH.
    echo 👉 Please install Python 3.10+ and add it to PATH.
    pause
    exit /b
)

echo.
echo ---------------------------------------------
echo 📦 Installing required libraries from requirements.txt...
echo ---------------------------------------------
IF EXIST requirements.txt (
    python -m pip install --upgrade pip
    pip install -r requirements.txt
) ELSE (
    echo ⚠️ requirements.txt file not found. Skipping dependency installation.
)

echo.
echo ---------------------------------------------
echo 🚀 Launching the Streamlit App...
echo ---------------------------------------------
IF EXIST app.py (
    streamlit run app.py
) ELSE (
    echo ❌ app.py not found! Make sure the file exists in this folder.
    pause
    exit /b
)

pause
