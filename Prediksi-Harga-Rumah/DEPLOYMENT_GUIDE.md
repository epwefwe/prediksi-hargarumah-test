# 🚀 Panduan Deployment Streamlit - Prediksi Harga Rumah

## 📋 Persyaratan Sistem
- Python 3.8+
- pip (Python package manager)
- Git (opsional)

## 🏗️ Struktur Proyek
```
Prediksi-Harga-Rumah/
├── src/
│   ├── streamlit.py          # Main Streamlit app
│   ├── api.py                # FastAPI backend
│   ├── modelling.py          # Model training
│   ├── preprocessing.py      # Data preprocessing
│   ├── data_preparation.py   # Data preparation
│   └── util.py               # Utility functions
├── models/
│   ├── production_model.pkl  # Trained model
│   ├── ohe_stasiun.pkl      # Encoder
│   └── le_encoder.pkl        # Label encoder
├── data/
│   ├── raw/                  # Raw data
│   └── processed/            # Processed data
├── config/
│   └── params.yaml           # Configuration parameters
├── requirements.txt          # Python dependencies
├── .streamlit/
│   └── config.toml          # Streamlit configuration
├── run_streamlit.bat        # Windows batch script
└── run_streamlit.sh         # Linux/Mac shell script
```

## 🔧 Instalasi Lokal

### 1. Clone Repository (Jika menggunakan Git)
```bash
git clone <repository-url>
cd Prediksi-Harga-Rumah
```

### 2. Buat Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Jalankan Streamlit App

#### Cara 1: Menggunakan Script (Windows)
```bash
run_streamlit.bat
```

#### Cara 2: Menggunakan Script (Linux/Mac)
```bash
bash run_streamlit.sh
```

#### Cara 3: Manual
```bash
cd src
streamlit run streamlit.py
```

Aplikasi akan berjalan di: `http://localhost:8501`

## ☁️ Deployment ke Streamlit Cloud

### 1. Persiapan Repository GitHub
```bash
# Initialize git repo (jika belum ada)
git init
git add .
git commit -m "Initial commit"
git remote add origin <your-github-repo>
git push -u origin main
```

### 2. Deploy ke Streamlit Cloud
1. Buka https://share.streamlit.io
2. Login dengan akun GitHub
3. Klik "New app"
4. Pilih repository Anda
5. Pilih branch: `main`
6. Pilih file path: `src/streamlit.py`
7. Klik "Deploy"

**Catatan:** Pastikan file `requirements.txt` sudah ada di root folder.

## 🐳 Deployment Menggunakan Docker

### 1. Buat Dockerfile
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "src/streamlit.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### 2. Build Docker Image
```bash
docker build -t prediksi-harga-rumah .
```

### 3. Run Container
```bash
docker run -p 8501:8501 prediksi-harga-rumah
```

Aplikasi akan berjalan di: `http://localhost:8501`

## 🚀 Deployment ke Heroku

### 1. Install Heroku CLI
```bash
# Download dari https://devcenter.heroku.com/articles/heroku-cli
```

### 2. Buat Procfile
```
web: cd src && streamlit run streamlit.py --logger.level=error
```

### 3. Deploy
```bash
# Login ke Heroku
heroku login

# Create app
heroku create <app-name>

# Deploy
git push heroku main

# View logs
heroku logs --tail
```

Aplikasi akan berjalan di: `https://<app-name>.herokuapp.com`

## 🔐 Environment Variables (Opsional)

Jika menggunakan API eksternal atau credentials, buat file `.streamlit/secrets.toml`:

```toml
# .streamlit/secrets.toml
api_key = "your-api-key"
database_url = "your-database-url"
```

Akses di Streamlit:
```python
import streamlit as st
api_key = st.secrets["api_key"]
```

## 📊 Fitur Aplikasi

### 🔮 Tab Prediksi
- Input data properti dengan validasi real-time
- Prediksi harga rumah berdasarkan model ML
- Tampilan hasil dengan formatting currency
- Ringkasan data input

### 📈 Tab Informasi
- Informasi model dan dataset
- Deskripsi setiap variabel
- Panduan penggunaan

### ℹ️ Sidebar
- Informasi aplikasi
- Range data valid untuk setiap feature
- Status aplikasi

## ⚙️ Troubleshooting

### Error: "ModuleNotFoundError: No module named 'streamlit'"
```bash
pip install streamlit
```

### Error: "Model file not found"
- Pastikan file model ada di: `models/production_model.pkl`
- Pastikan path di `config/params.yaml` sudah benar

### Error: "Config file not found"
- Pastikan file `config/params.yaml` ada di root folder

### Streamlit tidak berjalan di port 8501
```bash
streamlit run src/streamlit.py --server.port 8000
```

## 📱 Responsiveness

Aplikasi sudah dioptimasi untuk:
- 📱 Mobile devices
- 💻 Tablet
- 🖥️ Desktop

## 🎨 Customization

### Mengubah Warna Theme
Edit `.streamlit/config.toml`:
```toml
[theme]
primaryColor = "#667eea"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"
```

### Mengubah Title dan Icon
Edit `src/streamlit.py`:
```python
st.set_page_config(
    page_title="Judul Baru",
    page_icon="🏠",
    layout="wide"
)
```

## 📝 Notes

- Model menggunakan Linear Regression
- Data sudah diproses dengan outlier removal
- Validasi data otomatis untuk memastikan input dalam range yang valid
- Prediksi ditampilkan dalam format currency (Rp)

## 📞 Support

Untuk masalah teknis:
1. Cek error message di console
2. Pastikan semua dependencies terinstall
3. Restart aplikasi
4. Cek file konfigurasi

## 📚 Referensi

- [Streamlit Documentation](https://docs.streamlit.io)
- [Streamlit Cloud Deployment](https://docs.streamlit.io/streamlit-cloud)
- [Docker Documentation](https://docs.docker.com)
- [Heroku Deployment](https://devcenter.heroku.com)

---
Last Updated: 2024
