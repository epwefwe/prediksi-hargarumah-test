# 🏠 Prediksi Harga Rumah di Tebet

Aplikasi Machine Learning untuk prediksi harga rumah di area Tebet, Jakarta menggunakan Linear Regression Model dengan User Interface berbasis Streamlit.

## 📊 Dataset
- **Sumber:** https://www.kaggle.com/datasets/wisnuanggara/daftar-harga-rumah
- **Area:** Tebet, Jakarta
- **Target Variable:** HARGA (Harga Rumah dalam Rp)

## 📁 Struktur Proyek

### 📓 Jupyter Notebooks
- `data_preparation.ipynb` - Data cleaning, splitting & validation
- `eda.ipynb` - Exploratory Data Analysis, korelasi, dan deteksi outlier
- `preprocessing.ipynb` - Outlier removal dan feature engineering
- `modelling.ipynb` - Model training dan evaluation

### 🐍 Python Modules
- `src/data_preparation.py` - Data validation & checking
- `src/preprocessing.py` - Data preprocessing & cleaning
- `src/modelling.py` - Model training pipeline
- `src/api.py` - FastAPI backend (optional)
- `src/streamlit.py` - **Main UI Application** ⭐
- `src/util.py` - Utility functions

### 📦 Models & Data
- `models/production_model.pkl` - Trained Linear Regression model
- `models/ohe_stasiun.pkl` - One-Hot Encoder
- `models/le_encoder.pkl` - Label Encoder
- `config/params.yaml` - Configuration parameters

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Streamlit App
```bash
# Windows
run_streamlit.bat

# Linux/Mac
bash run_streamlit.sh

# Manual
cd src
streamlit run streamlit.py
```

Aplikasi akan berjalan di: **http://localhost:8501**

## 🎨 Features

### 🔮 Prediksi Harga
- Input interaktif untuk 6 feature properti
- Validasi data real-time
- Prediksi harga instant
- Tampilan hasil dengan format currency

### 📈 Informasi Model
- Model information dan dataset overview
- Deskripsi setiap variabel
- Range data valid untuk setiap feature

### ℹ️ Sidebar
- Panduan penggunaan
- Range data specifications
- Status aplikasi

## 📋 Input Features

| Feature | Deskripsi | Range |
|---------|-----------|-------|
| **HARGA** | Harga rumah (Rp) | 300M - 70M |
| **LB** | Luas bangunan (m²) | 30 - 2000 |
| **LT** | Luas tanah (m²) | 20 - 2000 |
| **KT** | Jumlah kamar tidur | 1 - 15 |
| **KM** | Jumlah kamar mandi | 1 - 15 |
| **GRS** | Kapasitas garasi | 0 - 15 |

## ☁️ Deployment Options

### Lokal Development
```bash
streamlit run src/streamlit.py
```

### Docker
```bash
docker build -t prediksi-harga-rumah .
docker run -p 8501:8501 prediksi-harga-rumah
```

### Docker Compose
```bash
docker-compose up
```

### Streamlit Cloud
1. Push ke GitHub
2. Login ke https://share.streamlit.io
3. Deploy dengan 1 klik

### Heroku
```bash
git push heroku main
```

📚 **Lihat [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) untuk panduan lengkap deployment**

## 🔧 Model Information

- **Algorithm:** Linear Regression
- **Evaluation Metrics:**
  - Cross-validation RMSE
  - Mean Absolute Error (MAE)
  - Mean Squared Error (MSE)
- **Data Processing:** Outlier removal, normalization
- **Status:** Production Ready ✅

## 📊 Data Pipeline

```
Raw Data
    ↓
Data Preparation (validation, splitting)
    ↓
EDA (exploration, visualization)
    ↓
Preprocessing (cleaning, outlier removal)
    ↓
Modelling (training, evaluation)
    ↓
Deployment (Streamlit UI)
```

## 🛠️ Configuration

Edit `config/params.yaml` untuk mengubah:
- Paths untuk data dan models
- Range nilai untuk setiap feature
- Threshold untuk outlier detection

## 📱 Responsive Design

Aplikasi dapat diakses dari:
- 🖥️ Desktop browsers
- 💻 Laptop/Tablet
- 📱 Mobile phones

## 🐛 Troubleshooting

**Error: Model file not found**
- Pastikan file `models/production_model.pkl` ada
- Cek path di `config/params.yaml`

**Error: Config file not found**
- Pastikan `config/params.yaml` ada di root directory

**Port 8501 sudah terpakai**
```bash
streamlit run src/streamlit.py --server.port 8000
```

## 📝 Requirements

- Python 3.8+
- pandas
- numpy
- scikit-learn
- streamlit
- joblib
- pyyaml

## 📞 Support

Untuk masalah teknis, cek:
1. Log error di console
2. Dependencies installation
3. File configuration
4. Model file existence

## 📚 Additional Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [Scikit-learn Linear Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)
- [Kaggle Dataset](https://www.kaggle.com/datasets/wisnuanggara/daftar-harga-rumah)

---
**Version:** 2.0 (Updated with Streamlit UI)  
**Last Updated:** December 2024
 