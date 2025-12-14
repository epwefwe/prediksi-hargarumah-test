# ☁️ Cloud Platform Deployment Guide

## Comparison of Cloud Platforms

| Platform | Cost | Ease | Scaling | Setup Time |
|----------|------|------|---------|------------|
| Streamlit Cloud | Free | ⭐⭐⭐⭐⭐ | Auto | 2 min |
| Heroku | $ | ⭐⭐⭐⭐ | Manual | 5 min |
| Railway | $ | ⭐⭐⭐⭐ | Auto | 5 min |
| Render | $ | ⭐⭐⭐⭐ | Auto | 5 min |
| PythonAnywhere | $ | ⭐⭐⭐ | Manual | 10 min |
| AWS | $$$ | ⭐⭐⭐ | Auto | 20 min |
| Google Cloud | $$$ | ⭐⭐⭐ | Auto | 20 min |
| Azure | $$$ | ⭐⭐⭐ | Auto | 20 min |

---

## 1. Streamlit Cloud (Recommended - Easiest) ⭐

**Pros:**
- Free tier available
- 1-click deployment from GitHub
- Automatic redeploy on git push
- No infrastructure management
- Built-in SSL

**Setup:**

```bash
# 1. Push to GitHub
git push origin main

# 2. Go to https://share.streamlit.io
# 3. Click "New app"
# 4. Select repository and main file path
# 5. Deploy!
```

**Access:** `https://prediksi-harga-rumah.streamlit.app`

**Limitations:**
- Free tier: 1GB RAM, limited CPU
- App goes idle after 1 hour of inactivity
- Cold start takes ~30 seconds

---

## 2. Heroku

**Pros:**
- Easy deployment
- Free tier (with credit card)
- Good documentation
- Easy environment variables

**Setup:**

```bash
# 1. Install Heroku CLI
# https://devcenter.heroku.com/articles/heroku-cli

# 2. Create Procfile (already in repo)
# 3. Login
heroku login

# 4. Create app
heroku create prediksi-harga-rumah

# 5. Deploy
git push heroku main

# 6. View app
heroku open
```

**Access:** `https://prediksi-harga-rumah.herokuapp.com`

**Cost:**
- Free tier: $0 (with dyno hours limit)
- Pro: $7/month

---

## 3. Railway

**Pros:**
- Modern, fast deployment
- Good free tier
- Simple UI
- Pay-as-you-go pricing

**Setup:**

```bash
# 1. Go to https://railway.app
# 2. Login with GitHub
# 3. Create new project
# 4. Select "Deploy from GitHub repo"
# 5. Configure and deploy
```

**Cost:** $5 credit/month, pay-as-you-go after

---

## 4. Render

**Pros:**
- Free tier with auto-deploy
- Simple configuration
- Native support for Streamlit
- Fast deployments

**Setup:**

```bash
# 1. Go to https://render.com
# 2. Login with GitHub
# 3. Create new "Web Service"
# 4. Select repository
# 5. Configure:
#    - Build command: pip install -r requirements.txt
#    - Start command: cd src && streamlit run streamlit.py
# 6. Deploy
```

**Cost:** Free tier available, paid plans from $7/month

---

## 5. PythonAnywhere

**Pros:**
- Python-focused platform
- Good for beginners
- Terminal access
- File management

**Setup:**

```bash
# 1. Register at https://www.pythonanywhere.com
# 2. Upload files via web interface
# 3. Create web app
# 4. Configure WSGI file
# 5. Set up virtual environment
# 6. Install dependencies
# 7. Reload app
```

**Cost:** Free tier limited, paid from $5/month

---

## 6. AWS EC2

**Pros:**
- Full control
- Scalable
- Enterprise-grade
- Many services available

**Setup:**

```bash
# 1. Create EC2 instance (Ubuntu, free tier eligible)
# 2. SSH into instance
ssh -i key.pem ubuntu@ec2-instance.amazonaws.com

# 3. Install Python & dependencies
sudo apt update
sudo apt install python3-pip python3-venv
pip install -r requirements.txt

# 4. Run Streamlit
cd src
streamlit run streamlit.py

# 5. Use systemd to keep app running
# Create /etc/systemd/system/streamlit.service
```

**Cost:** 
- Free tier: 750 hours/month
- t2.micro instance sufficient
- Pay-as-you-go beyond free tier

**Setup Systemd Service:**

```ini
[Unit]
Description=Streamlit App
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu/Prediksi-Harga-Rumah/src
ExecStart=/usr/bin/python3 -m streamlit run streamlit.py --server.port 80
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

---

## 7. Google Cloud Run

**Pros:**
- Serverless (pay per request)
- Auto-scaling
- Very fast deployment
- Good for sporadic traffic

**Setup:**

```bash
# 1. Create GCP project
gcloud projects create prediksi-harga-rumah

# 2. Build & push image
gcloud builds submit --tag gcr.io/PROJECT_ID/prediksi

# 3. Deploy to Cloud Run
gcloud run deploy prediksi-harga-rumah \
  --image gcr.io/PROJECT_ID/prediksi \
  --platform managed \
  --region us-central1 \
  --memory 1Gi \
  --port 8501

# 4. Get URL
gcloud run services describe prediksi-harga-rumah
```

**Cost:**
- Free tier: 2M invocations/month
- $0.00001667 per invocation
- Storage charges for container image

---

## 8. Azure Container Instances

**Pros:**
- Easy Docker deployment
- Pay-per-second
- No infrastructure management
- Good integration with Azure services

**Setup:**

```bash
# 1. Create resource group
az group create --name rg-prediksi --location eastus

# 2. Create ACR
az acr create --resource-group rg-prediksi \
  --name prediksiregistry --sku Basic

# 3. Push image (see Docker guide)

# 4. Deploy container
az container create \
  --resource-group rg-prediksi \
  --name prediksi-app \
  --image prediksiregistry.azurecr.io/prediksi:latest \
  --ports 8501 \
  --cpu 1 --memory 1.0
```

**Cost:**
- Pay-per-second for compute
- Free tier available (limited)
- ~$0.0125/hour for 1 CPU, 1GB RAM

---

## 9. DigitalOcean App Platform

**Pros:**
- Simple interface
- Fixed pricing
- Good documentation
- GitHub integration

**Setup:**

```bash
# 1. Go to https://www.digitalocean.com
# 2. Create new App
# 3. Connect GitHub
# 4. Select repository
# 5. Configure app.yaml
# 6. Deploy
```

**Cost:** $12/month (all-inclusive)

**app.yaml:**
```yaml
name: prediksi-harga-rumah
services:
- name: streamlit
  github:
    repo: username/Prediksi-Harga-Rumah
    branch: main
  build_command: pip install -r requirements.txt
  run_command: cd src && streamlit run streamlit.py
  http_port: 8501
```

---

## Environment Variables Setup

### Streamlit Cloud

1. App Settings → Secrets
2. Add secrets in TOML format

```toml
# .streamlit/secrets.toml
api_key = "xxx"
database_url = "xxx"
```

### Heroku

```bash
heroku config:set API_KEY=xxx DATABASE_URL=xxx
```

### Render

Dashboard → Environment → Add Variable

### AWS EC2

```bash
export API_KEY=xxx
export DATABASE_URL=xxx
```

Or edit `.env` and load in app:
```python
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv('API_KEY')
```

---

## Domain Setup

### Custom Domain (All Platforms)

1. Buy domain (Namecheap, GoDaddy, etc.)
2. Update DNS records to platform's nameservers
3. Configure in platform settings
4. Wait for DNS propagation (24-48 hours)

---

## SSL/HTTPS

Most platforms provide free SSL by default:
- ✅ Streamlit Cloud
- ✅ Heroku
- ✅ Railway
- ✅ Render
- ✅ Google Cloud Run
- ✅ Azure Container Instances
- ✅ DigitalOcean

---

## Monitoring & Logs

### Streamlit Cloud
- Dashboard → Logs

### Heroku
```bash
heroku logs --tail
```

### Railway
- Dashboard → Logs

### Google Cloud Run
```bash
gcloud run logs read prediksi-harga-rumah
```

### AWS EC2
```bash
sudo journalctl -u streamlit -f
```

---

## Cost Comparison (Monthly)

| Service | Free Tier | Paid Starting |
|---------|-----------|---------------|
| Streamlit Cloud | ✅ Yes | - |
| Heroku | ⚠️ Limited | $7 |
| Railway | ✅ Yes | Pay-as-you-go |
| Render | ✅ Yes | $7 |
| Google Cloud Run | ✅ Yes | ~$0 (pay-per-request) |
| Azure | ✅ Limited | ~$10 |
| AWS | ✅ Limited | ~$10-20 |
| DigitalOcean | ❌ No | $12 |

---

## Recommendation

**For Production:** Streamlit Cloud (free, easiest, sufficient for most use cases)
**For Scalability:** Google Cloud Run (pay-per-request, auto-scale)
**For Full Control:** AWS EC2 or DigitalOcean (more complex but flexible)
**For Simplicity:** Railway or Render (good balance of ease and features)

---

## Next Steps

1. Choose platform based on your needs
2. Follow setup guide for that platform
3. Deploy app
4. Monitor performance
5. Update and maintain regularly

For questions, check platform-specific documentation or community forums.
