# Adding a Custom Icon (Optional)

## Quick Method - Use Online Converter

1. Find or create a PNG image (512x512 recommended)
2. Go to: https://convertio.co/png-ico/
3. Upload your PNG and convert to ICO format
4. Download the ICO file
5. Save as `icon.ico` in the project folder
6. Build with icon:
   ```bash
   pyinstaller --onefile --windowed --name "CountdownTimer" --icon=icon.ico countdown_timer.py
   ```

## Icon Design Suggestions

For a countdown timer, consider:
- ⏱️ Clock or stopwatch icon
- ⏲️ Timer icon
- ⏰ Alarm clock icon
- 🕐 Simple clock face
- ⏳ Hourglass icon

## Using Windows Built-in Icons

You can extract icons from Windows system files:
```bash
# Use icons from shell32.dll
pyinstaller --onefile --windowed --name "CountdownTimer" --icon="C:\Windows\System32\shell32.dll,16" countdown_timer.py
```

Common shell32.dll icon indices:
- 16: Question mark
- 23: Folder
- 24: Open folder
- 41: Delete/Recycle
- 109: Mail
- 165: Video
- 210: Information

## No Icon Build

If you don't want to add an icon, the current build command works perfectly:
```bash
pyinstaller --onefile --windowed --name "CountdownTimer" countdown_timer.py
```

The EXE will use the default Python icon.

## Free Icon Resources

- Flaticon: https://www.flaticon.com
- Icons8: https://icons8.com
- Iconfinder: https://www.iconfinder.com
- Font Awesome: https://fontawesome.com

Remember to check the license before using any icon!
