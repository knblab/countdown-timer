# PowerShell User Guide

## ⚠️ Important: Running Scripts in PowerShell

In PowerShell, you must prefix local scripts with `.\` (dot-slash)

## 🚀 Quick Commands

### Run the Application
```powershell
python countdown_timer.py
```

### Build the EXE (Recommended)
```powershell
.\build.ps1
```

### Alternative: Build with Batch File
```powershell
.\build.bat
```

### Quick Test Run
```powershell
.\run.bat
```

## 🔧 Why `.\` is Required

PowerShell doesn't run scripts from the current directory by default for security reasons.

**Wrong:**
```powershell
build.bat          # ❌ Error: CommandNotFoundException
```

**Correct:**
```powershell
.\build.bat        # ✅ Works!
```

## 📦 Building Your EXE - Step by Step

### Method 1: Automated Build (Recommended)

```powershell
# Navigate to project folder (if not already there)
cd C:\Users\lenovo\Documents\CountDownTimer

# Run the PowerShell build script
.\build.ps1

# Or run the batch script
.\build.bat

# Find your EXE at: dist\CountdownTimer.exe
```

### Method 2: Manual Build

```powershell
# Install PyInstaller (one time only)
pip install pyinstaller

# Build the EXE
pyinstaller --onefile --windowed --name "CountdownTimer" countdown_timer.py

# Your EXE is now at: dist\CountdownTimer.exe
```

## 🎯 Common PowerShell Commands

```powershell
# Check if you're in the right folder
pwd
# Should show: C:\Users\lenovo\Documents\CountDownTimer

# List all files
ls
# or
dir

# Run the Python application
python countdown_timer.py

# Check Python version
python --version

# Check if PyInstaller is installed
pip show pyinstaller

# Install PyInstaller
pip install pyinstaller

# Build the EXE
.\build.ps1
```

## 🐛 Troubleshooting

### Problem: Script Execution Policy Error

If you see: `cannot be loaded because running scripts is disabled`

**Solution:**
```powershell
# Option 1: Run with bypass (one-time)
powershell -ExecutionPolicy Bypass -File .\build.ps1

# Option 2: Change policy (permanent)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then run:
```powershell
.\build.ps1
```

### Problem: Python not recognized

**Solution:**
```powershell
# Check if Python is installed
python --version

# If not found, download from: https://www.python.org/downloads/
# Make sure to check "Add Python to PATH" during installation
```

### Problem: pip not recognized

**Solution:**
```powershell
# Use python -m pip instead
python -m pip install pyinstaller
```

## ✅ Quick Build Checklist

1. Open PowerShell
2. Navigate to project:
   ```powershell
   cd C:\Users\lenovo\Documents\CountDownTimer
   ```
3. Run build script:
   ```powershell
   .\build.ps1
   ```
4. Wait for completion (~30 seconds)
5. Find EXE at: `dist\CountdownTimer.exe`
6. Done! 🎉

## 🎨 Running the App

### Development Mode (with Python)
```powershell
python countdown_timer.py
```

### After Building EXE
```powershell
.\dist\CountdownTimer.exe
```

Or just double-click `CountdownTimer.exe` in Windows Explorer!

## 📝 Pro Tips

1. **Use Tab Completion**: Type `.\bui` and press TAB to autocomplete
2. **Use Up Arrow**: Press ↑ to recall previous commands
3. **Clear Screen**: Type `cls` to clear the console
4. **Open Explorer**: Type `explorer .` to open current folder
5. **Copy Path**: Shift + Right-click file → "Copy as path"

## 🚀 Full Build Example

Here's a complete PowerShell session:

```powershell
# Navigate to project
PS> cd C:\Users\lenovo\Documents\CountDownTimer

# Verify you're in the right place
PS> pwd
Path
----
C:\Users\lenovo\Documents\CountDownTimer

# Install PyInstaller (first time only)
PS> pip install pyinstaller

# Build the EXE
PS> .\build.ps1

# Wait for completion...
# ========================================
# Build completed successfully!
# ========================================
# 
# Your executable is located at:
#   dist\CountdownTimer.exe

# Test the EXE
PS> .\dist\CountdownTimer.exe

# Or open the folder
PS> explorer dist
```

## 🎯 Alternative: Using Command Prompt (CMD)

If you prefer CMD over PowerShell:

```cmd
cd C:\Users\lenovo\Documents\CountDownTimer
build.bat
```

In CMD, you don't need `.\` - just type `build.bat` directly!

## 📞 Need More Help?

- **Can't build?** → Check `CHECKLIST.md`
- **Can't run?** → Check `README.md`
- **Want to customize?** → Check `PROJECT_SUMMARY.md`
- **Need quick start?** → Check `QUICKSTART.md`

---

## ⭐ Summary

**Remember these two key commands:**

1. **Build EXE:**
   ```powershell
   .\build.ps1
   ```

2. **Run App:**
   ```powershell
   python countdown_timer.py
   ```

That's it! Happy coding! 🎉
