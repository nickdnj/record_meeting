# BlackHole QuickTime Manager

> **Vibe Coded from Idea to App in ~2 Hours with GPT-4.1 + o3-mini-high**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Platform: macOS](https://img.shields.io/badge/platform-macOS-blue)](https://existential.audio/blackhole/)

A modern, minimal Python desktop app for macOS to automate and simplify audio routing with the BlackHole virtual audio driver and manage QuickTime audio recordings. Designed for easy setup and reliable recording during Google Meet or other sessions.

---

## 🏁 Quick Install (macOS)

**Download:** [record_meeting 0.0.0.dmg](./record_meeting%200.0.0.dmg)

1. Open the DMG file.
2. Drag the `record_meeting.app` icon into your Applications folder.
3. Eject the DMG.
4. Run the app from Applications.

No Python or setup required!

---

## 🚀 Vibe Coded Provenance
This app was **completely vibe coded**: from idea to spec to code, using GPT-4.1 and o3-mini-high, in about 2 hours. Every line, every feature, every UX detail was generated and iterated in a single creative session—no legacy code, no boilerplate, just pure flow.

- **Spec, design, and code:** All AI-generated, guided by user intent.
- **Stack:** Python 3.8+, PyQt5, macOS system tools, AppleScript.
- **Goal:** Make BlackHole + QuickTime recording dead simple for anyone.

---

## ✨ Features
- Detects BlackHole installation and guides setup
- Automates (or guides) Multi-Output Device creation
- Sets Multi-Output Device as default output
- Launches QuickTime Player in audio recording mode (with BlackHole as input)
- Start/stop recording with a single click
- Saves recordings to a user-specified directory with custom naming
- Restores previous audio settings after recording
- Real-time log and status updates
- Modern, minimal PyQt5 interface
- Configuration panel for save location, filename, and more

---

## 🖥️ Requirements
- macOS (Intel or Apple Silicon)
- Python 3.8+
- [BlackHole](https://existential.audio/blackhole/) (must be installed separately)
- QuickTime Player (pre-installed on macOS)

---

## ⚡ Installation
1. **Clone this repository:**
   ```bash
   git clone https://github.com/yourusername/record_meeting.git
   cd record_meeting
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Install BlackHole:**
   Download and install from [existential.audio/blackhole](https://existential.audio/blackhole/).

---

## 🎬 Usage
```bash
python main.py
```
- Use the UI to set up audio routing, start/stop recordings, and manage settings.
- Logs and status updates are shown in the main window.

---

## 📦 Distribution & Installation

See [DISTRIBUTION.md](DISTRIBUTION.md) for detailed instructions on:
- **Standalone Executable:** How to build and share a one-click Mac app using PyInstaller.
- **Running from Source:** For developers and Python users.
- **Advanced Mac Packaging:** Creating a DMG, signing, and notarizing for a polished Mac experience.

---

## ⚙️ Configuration
- Access settings via the gear icon in the app.
- Change save location, filename conventions, and other preferences.

---

## 🤝 Contributing
Pull requests and issues are welcome! If you have ideas, bug reports, or want to help, open an issue or PR.

---

## 📄 License
MIT — see [LICENSE](LICENSE) for details.

---

## 🙏 Credits
- [BlackHole](https://existential.audio/blackhole/) by Existential Audio
- [PyQt5](https://riverbankcomputing.com/software/pyqt/intro/)
- [GPT-4.1](https://openai.com/research/gpt-4) + o3-mini-high for the creative coding session

---

## 💡 About This Project
This project is a testament to the power of AI-assisted, vibe-driven development. From blank slate to working app, everything here was generated, refined, and shipped in a single, creative, two-hour session. If you use it, star it, or remix it—let us know! 