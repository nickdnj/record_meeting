# Distribution & Installation Guide

This guide explains how to share, install, and run **BlackHole QuickTime Manager** on any Mac, whether your users are developers or just want a one-click app experience.

---

## 1. Standalone Executable (Recommended for Most Users)

**Bundle your app as a single Mac executable using [PyInstaller](https://pyinstaller.org/).**

### Automated Build Script
Use the provided `build_dmg.sh` script to automate the entire process:

```bash
chmod +x build_dmg.sh
./build_dmg.sh
```
- This will clean old builds, convert your custom icon, build the `.app` with PyInstaller, and create a DMG installer.
- Make sure your `icon.png` is present in the project directory.

### Troubleshooting
- **DMG already exists:** If you see an error about the DMG already existing, delete old DMG files before running the script.
- **Unsigned app warning:** You may see a warning about code signing. The DMG and app will still work, but users may need to right-click → Open the first time.
- **Custom icon:** The DMG and app will display your custom icon everywhere on macOS.

---

## 2. Running from Source (For Developers)

**Best for users who already have Python 3.8+ installed.**

### Steps
1. **Clone the repo:**
   ```bash
   git clone https://github.com/yourusername/record_meeting.git
   cd record_meeting
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the app:**
   ```bash
   python main.py
   ```

---

## 3. Advanced: DMG Packaging, Signing, and Notarization

**For a polished, Mac-native experience and public distribution.**

### a) Create a .app Bundle
- PyInstaller with `--windowed` creates a `.app` bundle in `dist/`.

### b) Create a DMG Installer
- Use [create-dmg](https://github.com/sindresorhus/create-dmg) or similar tools:
  ```bash
  npm install -g create-dmg
  create-dmg dist/record_meeting.app
  ```
- This creates a drag-and-drop installer for users.

### c) Code Signing & Notarization (Optional, for public distribution)
- **Sign your app** with an Apple Developer ID:
  ```bash
  codesign --deep --force --verify --verbose --sign "Developer ID Application: Your Name (TEAMID)" dist/record_meeting.app
  ```
- **Notarize** with Apple:
  - See [Apple's Notarization Guide](https://developer.apple.com/documentation/security/notarizing_macos_software_before_distribution)

**Note:** For sharing with friends, signing/notarization is not required. For mass/public distribution, it is recommended.

---

## 📝 Tips for Sharing
- Always test your build on a clean Mac (or a VM) if possible.
- For non-technical users, the standalone executable or DMG is easiest.
- If you update the app, repeat the build and share the new file.

---

## 📚 Resources
- [PyInstaller Documentation](https://pyinstaller.org/en/stable/)
- [create-dmg](https://github.com/sindresorhus/create-dmg)
- [Apple Notarization Guide](https://developer.apple.com/documentation/security/notarizing_macos_software_before_distribution)

---

If you have questions or want to contribute improvements to this guide, open an issue or PR! 