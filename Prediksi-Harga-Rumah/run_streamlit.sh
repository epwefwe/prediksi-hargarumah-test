#!/bin/bash
# Script untuk menjalankan Streamlit App

echo "Aktivasi virtual environment (jika ada)..."
if [ -f venv/bin/activate ]; then
    source venv/bin/activate
fi

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Starting Streamlit App..."
cd src
streamlit run streamlit.py
