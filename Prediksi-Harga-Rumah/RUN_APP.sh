#!/bin/bash
# ==========================================
# Streamlit App Launcher - Linux/Mac
# ==========================================
# Script untuk menjalankan Prediksi Harga Rumah Streamlit App

echo ""
echo "============================================"
echo "   Prediksi Harga Rumah - Streamlit App"
echo "============================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.8+ from https://www.python.org"
    exit 1
fi

echo "[✓] Python is installed"
echo ""

# Check if requirements.txt exists
if [ ! -f requirements.txt ]; then
    echo "ERROR: requirements.txt not found"
    echo "Please ensure you're in the project root directory"
    exit 1
fi

echo "[✓] requirements.txt found"
echo ""

# Create virtual environment if it doesn't exist
if [ ! -d venv ]; then
    echo "[*] Creating virtual environment..."
    python3 -m venv venv
    echo "[✓] Virtual environment created"
else
    echo "[✓] Virtual environment already exists"
fi

echo ""

# Activate virtual environment
echo "[*] Activating virtual environment..."
source venv/bin/activate
echo "[✓] Virtual environment activated"
echo ""

# Install/upgrade dependencies
echo "[*] Installing dependencies..."
pip install -q -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies"
    exit 1
fi
echo "[✓] Dependencies installed"
echo ""

# Check if streamlit.py exists
if [ ! -f src/streamlit.py ]; then
    echo "ERROR: src/streamlit.py not found"
    echo "Please ensure you're in the project root directory"
    exit 1
fi

echo "[✓] Streamlit app file found"
echo ""

# Start Streamlit app
echo "============================================"
echo "   Starting Streamlit Application..."
echo "============================================"
echo ""
echo "URL: http://localhost:8501"
echo "To stop the app, press Ctrl+C"
echo ""

cd src
streamlit run streamlit.py
