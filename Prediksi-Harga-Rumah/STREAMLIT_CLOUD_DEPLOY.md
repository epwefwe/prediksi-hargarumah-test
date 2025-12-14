# Streamlit Cloud Deployment Guide

## Prerequisites
- GitHub account
- Streamlit Cloud account (free at https://share.streamlit.io)
- Repository pushed to GitHub

## Step-by-Step Deployment

### 1. Prepare Repository

Ensure your GitHub repository has:
- `requirements.txt` in root directory
- `src/streamlit.py` as the main app file
- `models/` folder with trained model
- `config/` folder with params.yaml
- All necessary data files

```bash
git add .
git commit -m "Prepare for Streamlit Cloud deployment"
git push origin main
```

### 2. Login to Streamlit Cloud

1. Visit https://share.streamlit.io
2. Click "Sign in with GitHub"
3. Authorize Streamlit

### 3. Deploy New App

1. Click "New app" button
2. Select your GitHub repository
3. Fill in the deployment details:
   - **Repository:** IlhamFM/Prediksi-Harga-Rumah
   - **Branch:** main
   - **Main file path:** src/streamlit.py
4. Click "Deploy"

Your app will be available at:
```
https://prediksi-harga-rumah.streamlit.app
```

### 4. Manage App Settings

In Streamlit Cloud dashboard:
- View logs: Settings → Logs
- Restart app: Settings → Reboot app
- Delete app: Settings → Delete app

### 5. Environment Variables (Optional)

If you need to store sensitive data:

1. Go to your app settings
2. Click "Secrets"
3. Add your secrets in TOML format

```toml
# .streamlit/secrets.toml
api_key = "your-key-here"
database_url = "your-db-url"
```

Access in app:
```python
import streamlit as st
api_key = st.secrets["api_key"]
```

## Troubleshooting

### App won't start
- Check logs in Streamlit Cloud
- Verify all files are in GitHub
- Ensure requirements.txt is in root

### ModuleNotFoundError
- Add package to requirements.txt
- Redeploy app

### Model file not found
- Ensure models/ folder is in GitHub
- Check path in config/params.yaml

## Update Deployed App

Simply push changes to GitHub:
```bash
git push origin main
```

Streamlit Cloud will automatically redeploy!

## Custom Domain (Optional)

1. In Streamlit Cloud settings
2. Click "Custom domain"
3. Add your domain
4. Update DNS records

## Performance Tips

- Use `@st.cache_resource` for model loading
- Minimize data loading with caching
- Optimize images before deployment
- Use session state for better UX

## Cost

- Free tier includes:
  - 1 deployment per GitHub account
  - 1GB RAM
  - 100x slower CPU
  
- Premium (paid) offers:
  - Unlimited deployments
  - More resources
  - Priority support

---

For more info: https://docs.streamlit.io/streamlit-cloud/deploy-your-app
