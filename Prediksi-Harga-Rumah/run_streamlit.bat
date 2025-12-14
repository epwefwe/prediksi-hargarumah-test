@echo off
REM Script untuk menjalankan Streamlit App

echo Aktivasi virtual environment (jika ada)...
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
)

echo Installing dependencies...
pip install -r requirements.txt

echo Starting Streamlit App...
cd src
streamlit run streamlit.py
