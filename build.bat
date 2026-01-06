@echo off
echo ========================================
echo Countdown Timer - Build Script
echo ========================================
echo.

echo Checking for PyInstaller...
pip show pyinstaller >nul 2>&1
if errorlevel 1 (
    echo PyInstaller not found. Installing...
    pip install pyinstaller
    if errorlevel 1 (
        echo Failed to install PyInstaller!
        pause
        exit /b 1
    )
    echo PyInstaller installed successfully!
) else (
    echo PyInstaller is already installed.
)

echo.
echo Cleaning previous build files...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist CountdownTimer.spec del /q CountdownTimer.spec

echo.
echo Building executable...
echo.
pyinstaller --onefile --windowed --name "CountdownTimer" --clean countdown_timer.py

if errorlevel 0 (
    echo.
    echo ========================================
    echo Build completed successfully!
    echo ========================================
    echo.
    echo Your executable is located at:
    echo   dist\CountdownTimer.exe
    echo.
    echo You can now copy this file anywhere and run it!
    echo.
) else (
    echo.
    echo Build failed! Please check the error messages above.
    echo.
)

pause
