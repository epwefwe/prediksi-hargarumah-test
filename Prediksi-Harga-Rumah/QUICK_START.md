# 🚀 Quick Start Guide

## Opsi 1: Run Streamlit Locally (Easiest)

### Windows
```bash
double-click RUN_APP.bat
```

### Linux/Mac
```bash
bash RUN_APP.sh
```

**Hasilnya:** Aplikasi berjalan di `http://localhost:8501`

---

## Opsi 2: Manual Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run App
```bash
cd src
streamlit run streamlit.py
```

---

## Opsi 3: Deploy ke Cloud (1-Click)

### Streamlit Cloud (Recommended)
1. Push repository ke GitHub
2. Buka https://share.streamlit.io
3. Login dengan GitHub
4. Click "New app" → Deploy
5. Done! ✅

---

## Opsi 4: Docker

### Run dengan Docker
```bash
docker-compose up
```

Access: `http://localhost:8501`

---

## Troubleshooting

| Error | Solusi |
|-------|--------|
| `ModuleNotFoundError` | Run: `pip install -r requirements.txt` |
| Port 8501 in use | Run: `streamlit run src/streamlit.py --server.port 8000` |
| Model not found | Cek file `models/production_model.pkl` ada |
| Config not found | Cek file `config/params.yaml` ada |

---

## Features

✨ **Prediksi Harga Rumah**
- Input data properti
- Validasi data real-time
- Hasil prediksi instant

📊 **Model Information**
- Linear Regression
- 6 features
- Production ready

---

## Next Steps

1. ✅ Run aplikasi
2. ✅ Test dengan data sample
3. ✅ Lihat documentation lengkap di `DEPLOYMENT_GUIDE.md`
4. ✅ Deploy ke cloud platform pilihan

---

## Documentation

- **[DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)** - Setup & deployment lokal/cloud
- **[DOCKER_DEPLOYMENT.md](DOCKER_DEPLOYMENT.md)** - Docker & container deployment
- **[CLOUD_DEPLOYMENT.md](CLOUD_DEPLOYMENT.md)** - Detailed cloud platform guides
- **[STREAMLIT_CLOUD_DEPLOY.md](STREAMLIT_CLOUD_DEPLOY.md)** - Streamlit Cloud specific
- **[README.md](README.md)** - Project overview

---

Happy predicting! 🎉
