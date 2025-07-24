# ADB-Control-Center

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/github/license/fufu25yt/ADB-Control-Center)](LICENSE)

[![logo](https://imgur.com/4MFhRgp)](https://github.com/fufu25yt/ADB-Control-Center)
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
```

### Run the app

```bash
python adb_control_center.py
```

✅ Tip: You can also create a .bat file for easier launching on Windows.

---

## 📱 How to Enable ADB on Your Phone

1. **Enable Developer Mode**

    Go to Settings > About phone  
    Tap Build number 7 times until you see “You are now a developer”

2. **Enable USB Debugging**

    Go to Settings > System > Developer options  
    Enable USB debugging

3. **(Optional) Connect via Wi-Fi**

    Connect the phone via USB first  
    Open ADB Control Center and use the Wi-Fi Connect tab  
    Enter the IP address (found in Wi-Fi settings) and click Connect

4. **Authorize your PC**

    When prompted on your phone:  
    “Allow USB debugging for this computer?”  
    → Tap Allow (and optionally check "Always allow")

---

## 📁 Project Structure (example)

```
adb_control_center/
├── adb_control_center.py
├── assets/
│   └── icons/
├── README.md
└── requirements.txt
```

---

## 📸 Screenshots

[https://i.imgur.com/UAJzzQy.png
](https://imgur.com/a/aRr6zv2)
---

## 🧩 Built With

- 🐍 Python
- 🎨 CustomTkinter
- 📡 ADB (Android Debug Bridge)

---

## 📃 License

This project is licensed under the MIT License.  
Feel free to use, modify, and share it.

---

## 📥 Download

🔗 https://github.com/fufu25yt/ADB-Control-Center/releases/tag/adb

---

## 🙌 Contributions

Pull requests, suggestions and improvements are welcome!  
Feel free to fork the repo and contribute 🤝
