# 🛡️ ChatGuard AI - Complete Installation Guide

## 📋 Table of Contents
1. [System Requirements](#system-requirements)
2. [Installation Steps](#installation-steps)
3. [Verification](#verification)
4. [Troubleshooting](#troubleshooting)
5. [First Run](#first-run)

---

## System Requirements

### Minimum Requirements
- **OS:** Windows 10+, Ubuntu 18.04+, macOS 10.14+
- **Python:** 3.8 or higher
- **RAM:** 4GB minimum
- **Disk Space:** 500MB free
- **Browser:** Chrome, Firefox, Safari, or Edge (any modern version)

### Recommended
- **Python:** 3.11 or 3.12
- **RAM:** 8GB+
- **SSD:** For faster installation
- **Internet:** Good connection for first-time setup

---

## Installation Steps

### 🪟 Windows Installation

#### Step 1: Install Python
1. Go to https://www.python.org/downloads/
2. Download Python 3.11 or 3.12
3. Run the installer
4. ⚠️ **IMPORTANT:** Check "Add Python to PATH"
5. Click "Install Now"
6. Verify installation:
   ```
   python --version
   ```

#### Step 2: Download ChatGuard AI
1. Download the `chatguard-ai.zip` file
2. Extract to desired location (e.g., `C:\Users\YourName\Desktop`)
3. Note the extracted folder path

#### Step 3: Run Setup
1. Open File Explorer
2. Navigate to the extracted folder
3. Double-click `setup.bat`
4. Wait for installation to complete (2-5 minutes)
5. Press Enter to close the window

#### Step 4: Start Application
1. In the same folder, double-click `run.bat`
2. Wait for: `Running on http://127.0.0.1:5000`
3. Open browser and go to: `http://127.0.0.1:5000`

---

### 🐧 Linux Installation

#### Step 1: Install Python (if not installed)
**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
python3 --version
```

**Fedora/RHEL:**
```bash
sudo dnf install python3 python3-pip
python3 --version
```

#### Step 2: Download ChatGuard AI
```bash
# Download and extract
unzip chatguard-ai.zip
cd chatguard-ai
ls -la
```

#### Step 3: Run Setup
```bash
chmod +x setup.sh
./setup.sh
```
This will take 2-5 minutes.

#### Step 4: Start Application
```bash
chmod +x run.sh
./run.sh
```

Then open: `http://127.0.0.1:5000`

---

### 🍎 macOS Installation

#### Step 1: Install Python (if not installed)
```bash
# Using Homebrew (recommended)
brew install python3
python3 --version

# OR download from https://www.python.org/downloads/
```

#### Step 2: Download ChatGuard AI
```bash
# Download and extract
unzip chatguard-ai.zip
cd chatguard-ai
ls -la
```

#### Step 3: Run Setup
```bash
chmod +x setup.sh
./setup.sh
```
This will take 2-5 minutes.

#### Step 4: Start Application
```bash
chmod +x run.sh
./run.sh
```

Then open: `http://127.0.0.1:5000`

---

## Verification

### Quick Verification
Run the verification script:

**Windows:**
```
python verify.py
```

**Linux/Mac:**
```bash
python3 verify.py
```

This will check all files and directories.

### Manual Verification
Check that these files exist:
- ✅ `chatguard-ai/backend/app.py`
- ✅ `chatguard-ai/frontend/index.html`
- ✅ `chatguard-ai/frontend/result.html`
- ✅ `chatguard-ai/frontend/style.css`
- ✅ `setup.bat` / `setup.sh`
- ✅ `run.bat` / `run.sh`
- ✅ `requirements.txt`

---

## Troubleshooting

### Issue: "Python not found"
**Windows:**
- Install Python from https://www.python.org/
- Check "Add Python to PATH" during installation
- Restart your computer
- Open new Command Prompt and try again

**Linux:**
```bash
sudo apt install python3
python3 --version
```

**Mac:**
```bash
brew install python3
python3 --version
```

### Issue: "Permission denied" on setup.sh
```bash
chmod +x setup.sh
./setup.sh
```

### Issue: "Port 5000 already in use"
The port is being used by another application.

**Windows:**
```bash
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

**Linux/Mac:**
```bash
lsof -i :5000
kill -9 <PID>
```

Or change the port in `app.py` line 15:
```python
app.run(host='127.0.0.1', port=5001, debug=True)  # Changed to 5001
```

### Issue: "Module not found" after setup
1. Delete the `venv` folder:
   ```bash
   rm -rf chatguard-ai/backend/venv
   ```
2. Run setup again:
   ```bash
   ./setup.sh  # or setup.bat on Windows
   ```

### Issue: Form doesn't submit
1. Open browser DevTools (F12)
2. Go to Console tab
3. Look for error messages
4. Common issues:
   - Backend not running
   - CORS error (check backend logs)
   - Network error (check port)

### Issue: Page shows "Not Found"
- Ensure backend is running on http://127.0.0.1:5000
- Check that files are extracted properly
- Clear browser cache (Ctrl+Shift+Delete)
- Try a different browser

---

## First Run

### Step 1: Confirm Server Running
You should see:
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

### Step 2: Open Browser
Go to: `http://127.0.0.1:5000`

### Step 3: Fill Test Form
Use this test data:
- **Transaction ID:** TEST123
- **Account Number:** 9876543210
- **User ID:** USER001
- **Email:** test@example.com
- **Phone:** 9999999999
- **Amount:** 5000
- **Prior Fraud:** No (unchecked)
- **Platform:** GOOGLE_PAY

### Step 4: Submit Form
Click "🔍 ANALYZE TRANSACTION"

### Step 5: View Results
You should see one of:
- ✅ **Safe** - Transaction approved
- ⚠️ **Suspicious** - Transaction flagged
- ❓ **Invalid** - Missing data

### Step 6: Stop Server
Press `Ctrl+C` in the terminal

---

## Advanced Configuration

### Change Port
Edit `chatguard-ai/backend/app.py`:
```python
app.run(host='127.0.0.1', port=8000, debug=True)  # Change 8000 to desired port
```

### Change Host (Network Access)
Edit `chatguard-ai/backend/app.py`:
```python
app.run(host='0.0.0.0', port=5000, debug=True)  # 0.0.0.0 allows external access
```

### Customize Settings
Edit `config.py`:
- `AMOUNT_THRESHOLD` - Fraud threshold
- `PLATFORMS_BLACKLIST` - Flagged platforms
- `DEBUG` - Debug mode

---

## Getting Help

1. **Check README.md** for detailed documentation
2. **Check QUICKSTART.md** for fast setup
3. **Review DEPLOYMENT.md** for distribution
4. **Run verify.py** to check installation
5. **Check browser console** (F12) for errors
6. **Check terminal logs** for backend errors

---

## Success Checklist

- [ ] Python 3.8+ installed
- [ ] Project extracted to folder
- [ ] setup.bat (Windows) or setup.sh (Linux/Mac) run successfully
- [ ] verify.py shows all checks passed
- [ ] run.bat (Windows) or run.sh (Linux/Mac) starts server
- [ ] Browser shows fraud detection form at http://127.0.0.1:5000
- [ ] Form submission works
- [ ] Results page displays verdict

---

**Congratulations! ChatGuard AI is ready to use! 🎉**

For questions or issues, refer to the documentation files or check the application logs.

---

**Last Updated:** November 12, 2025
**Version:** 1.0.0
**Status:** Production Ready
