# 🔧 Troubleshooting Guide

## Common Issues & Solutions

### 1. ModuleNotFoundError: No module named 'streamlit'

**Problem:** Streamlit tidak terinstall

**Solutions:**

```bash
# Install Streamlit
pip install streamlit

# Or install all dependencies
pip install -r requirements.txt

# Verify installation
python -c "import streamlit; print(streamlit.__version__)"
```

---

### 2. Port 8501 Already in Use

**Problem:** Port sudah digunakan oleh aplikasi lain

**Solutions:**

```bash
# Run on different port
streamlit run src/streamlit.py --server.port 8000

# Windows - Find and kill process on port 8501
netstat -ano | findstr :8501
taskkill /PID <PID> /F

# Linux/Mac - Find and kill process
lsof -ti:8501 | xargs kill -9
```

---

### 3. FileNotFoundError: models/production_model.pkl

**Problem:** Model file tidak ditemukan

**Solutions:**

```bash
# Check if file exists
ls models/production_model.pkl  # Linux/Mac
dir models                      # Windows

# Verify path in config/params.yaml
cat config/params.yaml | grep production_model_path

# If file missing - retrain model or restore from backup
# python src/modelling.py
```

---

### 4. FileNotFoundError: config/params.yaml

**Problem:** Configuration file tidak ditemukan

**Solutions:**

```bash
# Verify config exists
ls config/params.yaml  # Linux/Mac
dir config            # Windows

# Must be in root directory, not in src/
# Check current directory
pwd  # Linux/Mac
cd   # Windows
```

---

### 5. ModuleNotFoundError in streamlit.py

**Problem:** Import error dalam streamlit.py

**Check yang harus dilakukan:**

```bash
# 1. Verify file exists
ls -la src/streamlit.py

# 2. Check if path is correct
# Make sure running from project root, not from src/

# 3. Install missing modules
pip install -r requirements.txt

# 4. Check sys.path
python -c "import sys; print('\n'.join(sys.path))"
```

---

### 6. ModuleNotFoundError: No module named 'util'

**Problem:** util.py tidak ditemukan (import error dalam streamlit.py)

**Solution:**

```bash
# Make sure streamlit.py has correct import
# At top of src/streamlit.py should have:
# import sys
# from pathlib import Path
# sys.path.insert(0, str(Path(__file__).parent))
# import util as utils

# Or run from correct directory
cd /path/to/Prediksi-Harga-Rumah
streamlit run src/streamlit.py  # NOT: cd src && streamlit run streamlit.py
```

---

### 7. Streamlit App Won't Start

**Problem:** Error saat startup

**Debug steps:**

```bash
# Run with debug logging
streamlit run src/streamlit.py --logger.level=debug

# Check for Python syntax errors
python -m py_compile src/streamlit.py

# Test imports separately
python -c "import sys; sys.path.insert(0, 'src'); import streamlit"
```

---

### 8. Prediction Returns NaN or Invalid Results

**Problem:** Hasil prediksi tidak valid

**Solutions:**

```bash
# 1. Check input data validation
# - Ensure values are within valid range
# - Check config/params.yaml for range values

# 2. Verify model is loaded correctly
python -c "import joblib; model = joblib.load('models/production_model.pkl'); print(type(model))"

# 3. Test prediction with sample data
python << 'EOF'
import sys
sys.path.insert(0, 'src')
import joblib
import pandas as pd

model = joblib.load('models/production_model.pkl')
sample = pd.DataFrame({'HARGA': [5000000000], 'LB': [150], 'LT': [200], 'KT': [3], 'KM': [2], 'GRS': [2]})
print(model.predict(sample))
EOF
```

---

### 9. App Runs Slow

**Problem:** Aplikasi lambat atau timeout

**Solutions:**

```bash
# 1. Check system resources
# Windows
systeminfo | findstr /C:"System Boot Time"

# Linux/Mac
top

# 2. Optimize model loading - already uses @st.cache_resource

# 3. Check file sizes
ls -lh models/
ls -lh data/

# 4. Monitor memory usage while running
# Windows - use Task Manager
# Linux/Mac
while true; do top -bn1 | grep streamlit; sleep 1; done
```

---

### 10. Docker Container Won't Start

**Problem:** Docker container exits immediately

**Solutions:**

```bash
# Check logs
docker logs <container_id>

# Run in interactive mode to see error
docker run -it prediksi-harga-rumah /bin/bash

# Rebuild image
docker build --no-cache -t prediksi-harga-rumah .

# Check if requirements are correct
docker run --rm prediksi-harga-rumah python -m pip list
```

---

### 11. Database/API Connection Error

**Problem:** Tidak bisa connect ke database atau API

**Solutions:**

```bash
# 1. Test connectivity
ping <host>

# 2. Check if service is running
# Database - usually runs on specific port
netstat -an | grep LISTEN

# 3. Verify credentials in .streamlit/secrets.toml
cat .streamlit/secrets.toml

# 4. Test connection manually
python << 'EOF'
import os
db_url = os.getenv('DATABASE_URL')
print(f"Trying to connect to: {db_url}")
# Test connection logic
EOF
```

---

### 12. Memory Leak (App Gets Slower Over Time)

**Problem:** Aplikasi semakin lambat seiring waktu

**Solutions:**

```bash
# 1. Monitor memory usage
# Windows
Get-Process streamlit | Select-Object WorkingSet

# Linux/Mac
ps aux | grep streamlit

# 2. Restart container/app
docker restart <container_id>

# 3. Optimize code - use session state efficiently
# 4. Clear cache periodically

# 5. Check for memory leaks in code
python -m memory_profiler src/streamlit.py
```

---

### 13. Dependencies Conflict

**Problem:** pip install fails dengan dependency conflict

**Solutions:**

```bash
# 1. Create fresh virtual environment
python -m venv venv_new
source venv_new/bin/activate  # or venv_new\Scripts\activate on Windows

# 2. Upgrade pip
pip install --upgrade pip

# 3. Install requirements
pip install -r requirements.txt

# 4. Check for conflicts
pip check

# 5. If still fails, install one by one to find culprit
pip install streamlit
pip install pandas
# ... etc
```

---

### 14. YAML Config Not Parsed Correctly

**Problem:** Config values tidak terbaca dengan benar

**Solutions:**

```bash
# 1. Validate YAML syntax
python << 'EOF'
import yaml
with open('config/params.yaml', 'r') as f:
    params = yaml.safe_load(f)
    print(params)
EOF

# 2. Check for indentation (YAML uses spaces, not tabs)
cat -A config/params.yaml | grep "^I"  # Shows tabs as I

# 3. Ensure config/params.yaml is valid YAML
# Use online validator: https://www.yamllint.com/
```

---

### 15. Git Deployment Issues

**Problem:** Deployment dari GitHub gagal

**Solutions:**

```bash
# 1. Ensure all files committed
git status

# 2. Check requirements.txt
git ls-files | grep requirements.txt

# 3. Verify deployment files present
# For Streamlit Cloud:
git ls-files | grep -E "requirements.txt|.streamlit|src/streamlit.py"

# 4. Push changes
git add .
git commit -m "Fix deployment"
git push origin main

# 5. Check deployment logs on cloud platform
```

---

## Debugging Tools

### 1. Python Interactive Mode
```bash
python
>>> import sys
>>> sys.path.insert(0, 'src')
>>> import util as utils
>>> config = utils.load_params(...)
```

### 2. Print Debugging
```python
import streamlit as st
st.write("Debug output:", variable)
```

### 3. Logging
```python
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.debug("Debug message")
```

### 4. VS Code Debugger
```json
// .vscode/launch.json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Streamlit",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/src/streamlit.py",
            "console": "integratedTerminal",
            "justMyCode": true
        }
    ]
}
```

---

## Getting Help

### Before Asking for Help:

- [ ] Check this troubleshooting guide
- [ ] Check error message carefully
- [ ] Google the error message
- [ ] Check official documentation
- [ ] Check GitHub issues

### When Creating Issue:

Include:
- Full error message (screenshot is OK)
- Steps to reproduce
- What you've already tried
- Environment details (OS, Python version, etc.)
- Output of: `pip list`
- Output of: `python --version`

---

## Quick Sanity Checks

```bash
# 1. Test Python
python --version

# 2. Test pip
pip --version

# 3. Test imports
python -c "import streamlit, pandas, sklearn, yaml; print('All imports OK')"

# 4. Test model loading
python -c "import sys; sys.path.insert(0, 'src'); import util; print(util.dir_parent())"

# 5. Test file paths
ls models/production_model.pkl config/params.yaml data/processed/

# 6. Run streamlit with verbose output
streamlit run src/streamlit.py --logger.level=debug --client.logger.level=debug
```

---

## Performance Profiling

```bash
# CPU profiling
python -m cProfile -s cumulative src/streamlit.py

# Memory profiling
pip install memory-profiler
python -m memory_profiler src/streamlit.py

# Line profiling
pip install line_profiler
kernprof -l -v src/streamlit.py
```

---

## Still Not Working?

1. Delete virtual environment and start fresh
```bash
rm -rf venv  # Linux/Mac
rmdir /s venv  # Windows
python -m venv venv
```

2. Check Python compatibility
- Recommended: Python 3.8 - 3.10
- Test with different Python version

3. Check OS-specific issues
- Path separators (/ vs \)
- Line endings (LF vs CRLF)
- Permission issues

4. Reach out to support
- GitHub Issues
- Streamlit Community
- Stack Overflow

---

Last Updated: December 2024
