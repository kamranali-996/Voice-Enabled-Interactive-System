# 🎙️ Voice-Enabled Interactive Messaging System

**👨‍💻 Developed by: Kamran Ali
**🎓 Student at Shri Sant Gajanan Maharaj College of Engineering, Shegaon (Information Technology Department)**  
**💡 Project: Voice-Controlled Messaging & Application Assistant**  
**🗓️ Duration: 7-Day Python Development Internship (I Base Technology)**  

---

## 🧠 Project Overview

This Python-based project is a **Voice-Enabled Interactive System** that allows users to control both messaging and applications using voice commands. The system features:

- **🎤 Voice-controlled WhatsApp messaging**
- **🖥️ Voice-controlled application launching & closing**  
- **🔊 Real-time voice feedback using Text-to-Speech**
- **📊 Comprehensive activity logging system**
- **🌐 Web browser integration for popular sites**

---

## 🚀 Features

### 💬 Messaging System
- ✅ **Voice-controlled WhatsApp messaging**
- ✅ **Contact management with JSON configuration**
- ✅ **Automatic message scheduling**
- ✅ **Chat history logging**

### 🖥️ Application Control  
- ✅ **Voice-controlled app launching** (Notepad, Calculator, Chrome, etc.)
- ✅ **Website integration** (YouTube, Google, Gmail, WhatsApp Web)
- ✅ **Process management** (open/close applications)
- ✅ **Application activity logging**

---

## 🛠️ Installation

```bash
# Install required packages
pip install -r requirements.txt

🎮 Usage
Messaging System
bash
cd phase1
python voice_messaging.py
Commands: "Send message to [contact]", "Read my last message", "List contacts"

App Control System
bash
cd phase2
python voice_app_control.py
Commands: "Open [app]", "Close [app]", "List apps"

📁 Project Structure
text
Voice-Enabled-Interactive-System/
├── phase1/                 # Messaging system
│   ├── voice_messaging.py
│   ├── contacts.json
│   └── requirements.txt
├── phase2/                 # App control system
│   ├── voice_app_control.py
│   ├── apps_mapping.json
│   └── requirements.txt
├── logs/                   # Activity logs
│   ├── chat_logs.txt
│   └── app_logs.txt
├── requirements.txt        # Main dependencies
└── README.md
🏆 Technologies Used
Python - Core programming language

SpeechRecognition - Voice input processing

PyAudio - Microphone access

pyttsx3 - Text-to-speech engine

pywhatkit - WhatsApp automation

psutil - Application process management

<div align="center">
⭐ Star this repository if you find it helpful!

Built with ❤️ using Python

</div> ```
