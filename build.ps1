# Build script for creating portable EXE
# Run this script to build the Countdown Timer executable

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Countdown Timer - Build Script" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if PyInstaller is installed
Write-Host "Checking for PyInstaller..." -ForegroundColor Yellow
$pyinstallerCheck = pip show pyinstaller 2>$null

if (-not $pyinstallerCheck) {
    Write-Host "PyInstaller not found. Installing..." -ForegroundColor Yellow
    pip install pyinstaller
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Failed to install PyInstaller. Please install manually." -ForegroundColor Red
        exit 1
    }
    Write-Host "PyInstaller installed successfully!" -ForegroundColor Green
} else {
    Write-Host "PyInstaller is already installed." -ForegroundColor Green
}

Write-Host ""
Write-Host "Building executable..." -ForegroundColor Yellow
Write-Host ""

# Clean previous build files
if (Test-Path "build") {
    Remove-Item -Recurse -Force "build"
    Write-Host "Cleaned build directory" -ForegroundColor Gray
}
if (Test-Path "dist") {
    Remove-Item -Recurse -Force "dist"
    Write-Host "Cleaned dist directory" -ForegroundColor Gray
}
if (Test-Path "CountdownTimer.spec") {
    Remove-Item -Force "CountdownTimer.spec"
    Write-Host "Cleaned spec file" -ForegroundColor Gray
}

Write-Host ""

# Build the EXE
pyinstaller --onefile --windowed --name "CountdownTimer" --clean countdown_timer.py

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Green
    Write-Host "Build completed successfully!" -ForegroundColor Green
    Write-Host "========================================" -ForegroundColor Green
    Write-Host ""
    Write-Host "Your executable is located at:" -ForegroundColor Cyan
    Write-Host "  dist\CountdownTimer.exe" -ForegroundColor White
    Write-Host ""
    Write-Host "You can now copy this file anywhere and run it!" -ForegroundColor Yellow
    Write-Host ""
    
    # Show file size
    $exePath = "dist\CountdownTimer.exe"
    if (Test-Path $exePath) {
        $fileSize = (Get-Item $exePath).Length / 1MB
        Write-Host ("File size: {0:N2} MB" -f $fileSize) -ForegroundColor Gray
    }
} else {
    Write-Host ""
    Write-Host "Build failed! Please check the error messages above." -ForegroundColor Red
    Write-Host ""
    exit 1
}

Write-Host ""
Write-Host "Press any key to exit..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
