#!/usr/bin/env python3
"""
ChatGuard AI - Installation Verification Script
Run this to check if everything is set up correctly
"""

import os
import sys
from pathlib import Path

def check_file(path, description):
    """Check if a file exists"""
    if Path(path).exists():
        print(f"✅ {description}: {path}")
        return True
    else:
        print(f"❌ {description}: {path} - NOT FOUND")
        return False

def check_dir(path, description):
    """Check if a directory exists"""
    if Path(path).is_dir():
        print(f"✅ {description}: {path}")
        return True
    else:
        print(f"❌ {description}: {path} - NOT FOUND")
        return False

def main():
    print("\n" + "="*60)
    print("ChatGuard AI - Installation Verification")
    print("="*60 + "\n")
    
    checks = []
    
    # Check project structure
    print("📁 Checking Project Structure...")
    checks.append(check_dir("chatguard-ai", "Backend folder"))
    checks.append(check_dir("chatguard-ai/frontend", "Frontend folder"))
    checks.append(check_dir("chatguard-ai/data", "Data folder"))
    
    # Check backend files
    print("\n📄 Checking Backend Files...")
    checks.append(check_file("chatguard-ai/backend/app.py", "Flask app"))
    checks.append(check_file("chatguard-ai/backend/fraud_detection.py", "ML module"))
    checks.append(check_file("chatguard-ai/backend/requirements.txt", "Backend requirements"))
    
    # Check frontend files
    print("\n📄 Checking Frontend Files...")
    checks.append(check_file("chatguard-ai/frontend/index.html", "Main form"))
    checks.append(check_file("chatguard-ai/frontend/result.html", "Results page"))
    checks.append(check_file("chatguard-ai/frontend/style.css", "Styling"))
    
    # Check setup and run scripts
    print("\n🚀 Checking Setup & Run Scripts...")
    checks.append(check_file("setup.bat", "Windows setup script"))
    checks.append(check_file("setup.sh", "Linux/Mac setup script"))
    checks.append(check_file("run.bat", "Windows run script"))
    checks.append(check_file("run.sh", "Linux/Mac run script"))
    checks.append(check_file("run.py", "Universal Python runner"))
    
    # Check documentation
    print("\n📚 Checking Documentation...")
    checks.append(check_file("README.md", "Main documentation"))
    checks.append(check_file("QUICKSTART.md", "Quick start guide"))
    checks.append(check_file("DEPLOYMENT.md", "Deployment guide"))
    checks.append(check_file("config.py", "Configuration file"))
    
    # Check dependencies
    print("\n📦 Checking Dependencies...")
    checks.append(check_file("requirements.txt", "Root requirements"))
    
    # Check virtual environment
    print("\n🐍 Checking Virtual Environment...")
    if sys.platform == "win32":
        venv_check = check_dir("chatguard-ai/backend/venv/Scripts", "venv (Windows)")
    else:
        venv_check = check_dir("chatguard-ai/backend/venv/bin", "venv (Unix)")
    checks.append(venv_check)
    
    # Summary
    print("\n" + "="*60)
    passed = sum(checks)
    total = len(checks)
    percentage = (passed / total) * 100
    
    if passed == total:
        print(f"✅ ALL CHECKS PASSED! ({passed}/{total}) - 100%")
        print("\n🎉 Your installation is complete and ready to use!")
        print("\n📍 Next Steps:")
        if sys.platform == "win32":
            print("   1. Run: run.bat")
        else:
            print("   1. Run: ./run.sh")
        print("   2. Open: http://127.0.0.1:5000")
        print("   3. Fill the form and test fraud detection")
    else:
        print(f"⚠️  SOME CHECKS FAILED! ({passed}/{total}) - {percentage:.1f}%")
        print("\n❌ Missing files detected. Please:")
        print("   1. Ensure you downloaded the complete package")
        print("   2. Extract all files to the same directory")
        print("   3. Run setup script: setup.bat (Windows) or setup.sh (Linux/Mac)")
        print("   4. Run verification again")
    
    print("\n" + "="*60 + "\n")
    
    return 0 if passed == total else 1

if __name__ == "__main__":
    sys.exit(main())
