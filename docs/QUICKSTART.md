# Quick Start Guide - Countdown Timer

## 🚀 Run the Application Immediately

### Option 1: Run with Python
```bash
python countdown_timer.py
```

### Option 2: Build Portable EXE

**Easy Way (Just double-click):**
- Double-click `build.bat` 
- Wait for build to complete
- Find `CountdownTimer.exe` in the `dist` folder
- Done!

**Manual Way (Command line):**
```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name "CountdownTimer" countdown_timer.py
```

## 📖 How to Use

### Basic Timer Operation
1. **Set Time**: Enter minutes and seconds
2. **Start**: Click "Start" button
3. **Pause/Resume**: Click "Pause" to pause, click "Resume" to continue
4. **Reset**: Click "Reset" to stop and clear

### Theme & Display Options
- **Toggle Theme**: Switch between dark/light mode
- **Fullscreen**: Enter fullscreen mode (press ESC to exit)
- **Always on Top**: Pin window above other apps

### Keyboard Shortcuts
- **ESC**: Exit fullscreen mode

## ✨ Features at a Glance

| Feature | Description |
|---------|-------------|
| 🎨 **Themes** | Dark mode (default) and Light mode |
| 📺 **Fullscreen** | Borderless fullscreen display |
| ⏸️ **Pause/Resume** | Pause without losing progress |
| 🔔 **Sound Alert** | System beep when time's up |
| 📌 **Always on Top** | Keep timer visible over other windows |
| ⚡ **No Lag** | Smooth, responsive countdown |
| 📦 **Portable** | Single EXE file, no installation needed |

## 🛠️ Build Commands Reference

### Standard Build (Recommended)
```bash
pyinstaller --onefile --windowed --name "CountdownTimer" countdown_timer.py
```

### Debug Build (Shows console)
```bash
pyinstaller --onefile --name "CountdownTimer" countdown_timer.py
```

### With Custom Icon
```bash
pyinstaller --onefile --windowed --name "CountdownTimer" --icon=icon.ico countdown_timer.py
```

## 📁 Project Structure

```
CountDownTimer/
├── countdown_timer.py    # Main application source
├── README.md            # Full documentation
├── QUICKSTART.md        # This file
├── requirements.txt     # Python dependencies
├── build.bat           # Windows batch build script
├── build.ps1           # PowerShell build script
└── dist/               # Built executable (after building)
    └── CountdownTimer.exe
```

## ⚠️ Troubleshooting

**Problem**: EXE doesn't run
- Try building with debug mode (without `--windowed`)
- Check antivirus settings

**Problem**: No sound playing
- Check Windows volume settings
- Ensure sound is not muted

**Problem**: UI looks weird
- Try toggling theme
- Restart the application

## 🎯 Common Use Cases

### Pomodoro Timer
Set 25:00 minutes, click Start, focus on work!

### Cooking Timer
Set desired time, enable Always on Top, minimize to corner

### Workout Timer
Enter fullscreen mode for large display during exercise

### Presentation Timer
Use Always on Top during presentations to track time

## 💡 Tips

1. **Quick Reset**: Click Reset anytime to start over
2. **Theme Switching**: Works even while timer is running
3. **Fullscreen**: Use for distraction-free countdown
4. **Always on Top**: Great for keeping timer visible while working

---

**Need more details?** Check `README.md` for complete documentation.

**Ready to build?** Just run `build.bat` or `build.ps1`!
