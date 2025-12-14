# 📋 Deployment Checklist

## Pre-Deployment

### Code & Files
- [ ] All Python files are properly formatted
- [ ] No syntax errors in code
- [ ] requirements.txt is up to date
- [ ] All imports are available
- [ ] Model file exists: `models/production_model.pkl`
- [ ] Config file exists: `config/params.yaml`
- [ ] Data files are in correct location

### Testing
- [ ] Test app locally: `streamlit run src/streamlit.py`
- [ ] Test all input features work
- [ ] Test prediction function returns valid results
- [ ] Test with various input values
- [ ] Check error handling works correctly

### Documentation
- [ ] README.md is complete
- [ ] QUICK_START.md is present
- [ ] DEPLOYMENT_GUIDE.md is present
- [ ] Comments in code are clear
- [ ] Environment variables documented (if any)

### Security
- [ ] No sensitive data in code
- [ ] No hardcoded API keys
- [ ] No passwords in files
- [ ] .gitignore is properly configured
- [ ] Secrets are in .streamlit/secrets.toml (not committed)

### Performance
- [ ] Model loads correctly
- [ ] App responds within reasonable time
- [ ] No memory leaks detected
- [ ] Page layout is responsive

---

## Deployment Steps

### For Streamlit Cloud

- [ ] Create GitHub repository
- [ ] Push code to GitHub
- [ ] Create Streamlit Cloud account
- [ ] Login to https://share.streamlit.io
- [ ] Create new app from repository
- [ ] Verify app loads correctly
- [ ] Test predictions work
- [ ] Share app URL

### For Docker

- [ ] Dockerfile exists and is correct
- [ ] docker-compose.yml is configured
- [ ] .dockerignore is set up
- [ ] Build image: `docker build -t prediksi-harga-rumah .`
- [ ] Run container: `docker run -p 8501:8501 prediksi-harga-rumah`
- [ ] Verify app works in container
- [ ] Test predictions in containerized app

### For Heroku

- [ ] Heroku account created
- [ ] Heroku CLI installed
- [ ] Procfile exists
- [ ] Git repository initialized
- [ ] Create app: `heroku create prediksi-harga-rumah`
- [ ] Deploy: `git push heroku main`
- [ ] Verify app works: `heroku open`
- [ ] Check logs: `heroku logs --tail`

### For AWS EC2

- [ ] AWS account created
- [ ] EC2 instance launched
- [ ] Security group configured (port 8501 open)
- [ ] SSH access verified
- [ ] Python 3.8+ installed
- [ ] Code cloned to instance
- [ ] Dependencies installed
- [ ] Systemd service created
- [ ] Service enabled and started
- [ ] App accessible via public IP

---

## Post-Deployment

### Verification
- [ ] App URL accessible
- [ ] App loads in reasonable time
- [ ] All features work correctly
- [ ] Error handling works
- [ ] Performance is acceptable
- [ ] Mobile responsive

### Monitoring
- [ ] Set up logging (if applicable)
- [ ] Monitor resource usage
- [ ] Watch for error messages
- [ ] Check response times
- [ ] Monitor user activity (if applicable)

### Documentation
- [ ] Document deployment method used
- [ ] Document app URL
- [ ] Create runbook for common issues
- [ ] Document any custom configurations
- [ ] Share documentation with team

### Maintenance Plan
- [ ] Scheduled updates planned
- [ ] Backup strategy in place
- [ ] Monitoring alerts set up
- [ ] Incident response plan ready
- [ ] Version control strategy established

---

## Common Issues & Solutions

### Issue: App won't start
```bash
# Check logs
streamlit run src/streamlit.py --logger.level=debug
```

### Issue: Model file not found
```bash
# Verify file exists
ls -la models/production_model.pkl

# Check path in config/params.yaml
cat config/params.yaml | grep production_model_path
```

### Issue: Dependencies missing
```bash
# Update requirements
pip install -r requirements.txt

# Check what's installed
pip list
```

### Issue: Port already in use
```bash
# Use different port
streamlit run src/streamlit.py --server.port 8000

# On Linux/Mac - kill process on port 8501
lsof -ti:8501 | xargs kill -9
```

### Issue: Slow performance
- Check available RAM/CPU
- Optimize model loading (use caching)
- Check data size
- Monitor network latency

---

## Rollback Plan

If deployment fails:

1. **Local Development**
   - Revert code: `git checkout main`
   - Reinstall dependencies: `pip install -r requirements.txt`
   - Test locally first

2. **Streamlit Cloud**
   - GitHub → Revert commit
   - Cloud auto-redeploys from main

3. **Docker**
   - Docker → Run previous image version
   - `docker run prediksi-harga-rumah:previous-tag`

4. **Heroku**
   - Heroku → Rollback: `heroku releases:rollback`
   - Or redeploy from previous commit

5. **AWS EC2**
   - SSH to instance
   - `systemctl stop streamlit`
   - Fix issue
   - `systemctl start streamlit`

---

## Performance Benchmarks (Expected)

- **Model Load Time:** < 2 seconds
- **Prediction Time:** < 1 second
- **Page Load Time:** < 3 seconds
- **Memory Usage:** < 1GB
- **CPU Usage:** < 30%
- **Response Time:** < 5 seconds

---

## Sign-Off

| Role | Name | Date | Status |
|------|------|------|--------|
| Developer | | | |
| QA Lead | | | |
| DevOps | | | |
| Product Owner | | | |

---

## Notes

```
Add any additional notes or considerations:


```

---

Last Updated: December 2024
