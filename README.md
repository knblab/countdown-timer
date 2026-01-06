# ⏱️ Countdown Timer

A modern, portable Windows desktop countdown timer built with Python and Tkinter.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- 🎨 **Dual Themes** - Dark mode (default) and Light mode with instant switching
- 📺 **Fullscreen Mode** - Borderless fullscreen display (ESC to exit)
- ⏸️ **Pause/Resume** - Pause timer without losing progress
- 📌 **Always on Top** - Keep timer visible over other windows
- 🔔 **Sound Alert** - System beep notification when time is up
- ⚡ **Responsive UI** - Smooth, non-freezing countdown
- 📦 **Portable** - Single executable file, no installation required
- 🎯 **Large Display** - 120px font for easy reading from distance

## 🖼️ Preview

### Dark Mode (Default)
```
┌─────────────────────────────────────┐
│  Countdown Timer              ▭ □ ✕ │
├─────────────────────────────────────┤
│                                     │
│   Minutes: [  5  ]  Seconds: [ 30 ] │
│   [ Start ] [ Pause ] [ Reset ]     │
│                                     │
│            ┌─────────┐              │
│            │         │              │
│            │  05:30  │  ← 120px     │
│            │         │              │
│            └─────────┘              │
│                                     │
│   [🌓 Theme] [⛶ Full] [📌 Pin]     │
└─────────────────────────────────────┘
    Black BG + White Text
```

## 🚀 Quick Start

### Running with Python

```bash
# Clone the repository
git clone https://github.com/knblab/countdown-timer.git
cd countdown-timer

# Run the application
python countdown_timer.py
```

### Building Portable EXE

#### Windows (PowerShell)
```powershell
# Install PyInstaller
pip install pyinstaller

# Build using script
.\build.ps1

# Or build manually
pyinstaller --onefile --windowed --name "CountdownTimer" countdown_timer.py

# Find executable at: dist\CountdownTimer.exe
```

#### Windows (Command Prompt)
```cmd
pip install pyinstaller
build.bat
```

## 📖 Usage

1. **Set Timer**: Enter minutes and seconds
2. **Start**: Click Start button to begin countdown
3. **Pause/Resume**: Pause timer and resume from current position
4. **Reset**: Stop and clear the timer

### Controls

| Button | Function |
|--------|----------|
| Start | Begin countdown |
| Pause/Resume | Pause or continue timer |
| Reset | Stop and reset to 00:00 |
| 🌓 Toggle Theme | Switch between dark/light mode |
| ⛶ Fullscreen | Enter/exit fullscreen mode |
| 📌 Always on Top | Pin window above other apps |

### Keyboard Shortcuts

- **ESC** - Exit fullscreen mode

## 🎨 Themes

### Dark Mode (Default)
- Background: Black (#000000)
- Text: White (#FFFFFF)
- Perfect for low-light environments

### Light Mode
- Background: White (#FFFFFF)
- Text: Black (#000000)
- High contrast for bright environments

Toggle anytime with the 🌓 button!

## 🎯 Use Cases

- ⏰ **Pomodoro Timer** - 25-minute focus sessions
- 🍳 **Cooking Timer** - Track cooking times
- 🏋️ **Workout Timer** - Time exercise intervals
- 🎤 **Presentation Timer** - Track speaking time
- ☕ **Break Timer** - Short 5-10 minute breaks
- 📚 **Study Sessions** - 45-60 minute study blocks

## 🛠️ Requirements

### Development
- Python 3.7 or higher
- Tkinter (included with Python)
- Windows OS

### Running EXE
- Windows 7/8/10/11
- No Python installation required
- ~10 MB disk space

### Building
- PyInstaller 5.0+

## 📁 Project Structure

```
countdown-timer/
├── countdown_timer.py    # Main application
├── requirements.txt      # Python dependencies
├── build.bat            # Windows batch build script
├── build.ps1            # PowerShell build script
├── .gitignore           # Git ignore file
├── LICENSE              # MIT License
├── README.md            # This file
└── docs/                # Documentation
    ├── QUICKSTART.md
    ├── PROJECT_SUMMARY.md
    ├── VISUAL_GUIDE.md
    ├── CHECKLIST.md
    ├── ICON_GUIDE.md
    └── POWERSHELL_GUIDE.md
```

## 🔧 Build Commands

### Standard Build (Recommended)
```bash
pyinstaller --onefile --windowed --name "CountdownTimer" countdown_timer.py
```

### Debug Build (with console)
```bash
pyinstaller --onefile --name "CountdownTimer" countdown_timer.py
```

### With Custom Icon
```bash
pyinstaller --onefile --windowed --name "CountdownTimer" --icon=icon.ico countdown_timer.py
```

## 📚 Documentation

- **[Quick Start Guide](docs/QUICKSTART.md)** - Get started in 2 minutes
- **[Project Summary](docs/PROJECT_SUMMARY.md)** - Technical details and architecture
- **[Visual Guide](docs/VISUAL_GUIDE.md)** - UI layout and design specifications
- **[PowerShell Guide](docs/POWERSHELL_GUIDE.md)** - PowerShell-specific instructions
- **[Icon Guide](docs/ICON_GUIDE.md)** - Add custom icon to your EXE
- **[Checklist](docs/CHECKLIST.md)** - Testing and verification guide

## 🐛 Troubleshooting

### Application won't start
- Verify Python 3.7+ is installed: `python --version`
- Check Tkinter is available: `python -c "import tkinter"`

### EXE won't run
- Rebuild with `--windowed` flag
- Check antivirus/firewall settings
- Try on a different Windows machine

### No sound playing
- Check Windows sound settings
- Ensure system volume is not muted
- Test with other applications

### PowerShell script error
- Use `.\build.ps1` instead of `build.ps1`
- See [PowerShell Guide](docs/POWERSHELL_GUIDE.md) for details

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with Python and Tkinter
- Uses `winsound` for system beep notifications
- Packaged with PyInstaller

## 📧 Contact

Project Link: [https://github.com/knblab/countdown-timer](https://github.com/knblab/countdown-timer)

## ⭐ Show Your Support

Give a ⭐️ if this project helped you!

---

**Made with ❤️ using Python and Tkinter**
