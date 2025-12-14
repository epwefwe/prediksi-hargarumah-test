@echo off
REM ==========================================
REM Streamlit App Launcher - Windows
REM ==========================================
REM Script untuk menjalankan Prediksi Harga Rumah Streamlit App

echo.
echo ============================================
echo   Prediksi Harga Rumah - Streamlit App
echo ============================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org
    pause
    exit /b 1
)

echo [✓] Python is installed
echo.

REM Check if requirements.txt exists
if not exist requirements.txt (
    echo ERROR: requirements.txt not found
    echo Please ensure you're in the project root directory
    pause
    exit /b 1
)

echo [✓] requirements.txt found
echo.

REM Create virtual environment if it doesn't exist
if not exist venv (
    echo [*] Creating virtual environment...
    python -m venv venv
    echo [✓] Virtual environment created
) else (
    echo [✓] Virtual environment already exists
)

echo.

REM Activate virtual environment
echo [*] Activating virtual environment...
call venv\Scripts\activate.bat
echo [✓] Virtual environment activated
echo.

REM Install/upgrade dependencies
echo [*] Installing dependencies...
pip install -q -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
echo [✓] Dependencies installed
echo.

REM Check if streamlit.py exists
if not exist src\streamlit.py (
    echo ERROR: src\streamlit.py not found
    echo Please ensure you're in the project root directory
    pause
    exit /b 1
)

echo [✓] Streamlit app file found
echo.

REM Start Streamlit app
echo ============================================
echo   Starting Streamlit Application...
echo ============================================
echo.
echo URL: http://localhost:8501
echo To stop the app, press Ctrl+C
echo.

cd src
streamlit run streamlit.py

pause
