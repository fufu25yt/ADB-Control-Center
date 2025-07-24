# 📱 ADB Control Center

**Fully control your Android device from your PC — without touching the terminal.**  
A modern, intuitive GUI for ADB, built with Python and [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter).

---

## 🚀 Features

✅ **Device Management**
- Auto-detect connected devices (USB & Wi-Fi)
- Show full device info (model, Android version, battery, resolution)
- Connect to devices wirelessly via IP

📦 **App Control**
- List all apps (user + system)
- Uninstall, clear data, force stop, extract APKs
- Install APK files from your PC

📁 **File Transfer**
- Push/pull files or folders easily
- Browse local and device directories
- Create or delete files/folders on the device

🎮 **Controls & Input**
- Simulate key events: Home, Back, Power, Volume
- Perform swipe gestures
- Toggle Wi-Fi, Mobile Data, Airplane Mode, Dev Options

🧠 **Advanced Tools**
- Reboot (normal / recovery / bootloader)
- Capture screenshots
- View logcat logs
- Manage processes by PID or package
- View account list and app permissions

---

## 🛠 Installation

### Requirements

- [Python 3.8+](https://www.python.org/downloads/)
- [ADB](https://developer.android.com/studio/releases/platform-tools) installed and added to your system PATH

### Install dependencies

```bash
pip install customtkinter
