# 🕵️‍♂️ Advanced Python Keylogger with Real-Time Alerts

## 📌 Project Overview
This is a security research tool developed in Python that monitors keyboard input locally. Unlike basic loggers, this version includes **intelligent word filtering**, **audible alerts**, and **remote email notifications** when specific sensitive terms are detected.

### 🎯 Use Cases
* **Self-Monitoring:** Tracking your own typing habits or productivity.
* **Security Research:** Understanding how unauthorized software can intercept data (for educational purposes).
* **System Alerts:** Setting up triggers for specific commands to get notified if they are run on your machine.

---

## 🛠️ Implementation Details

### 1. The Core Engine (`pynput`)
The script uses the `pynput.keyboard` library to create a "Listener." This listener captures every keystroke and passes it to a function that cleans the data (converting special keys like `Space` or `Enter` into readable text) and saves it to `key_log.txt`.

### 2. Intelligent Triggers
I implemented a `typed_sequence` buffer. As you type, the script checks if the last string of characters matches any word in the `TRIGGER_WORDS` list (e.g., "password", "login").

### 3. Sound Notification (`pygame`)
To provide immediate feedback, I used the `pygame.mixer` library. When a trigger is hit, the script plays `beep.wav`. Using `pygame` instead of `playsound` ensures the script doesn't crash when multiple triggers happen quickly.

### 4. Email Alert System (`smtplib` & `ssl`)
The script connects to Gmail’s SMTP server via a secure SSL port (465). I used the modern `EmailMessage` class to ensure that emojis and special characters in the logs are encoded in **UTF-8** format, preventing "codec errors."

---

## 🚀 How to Set Up & Run

### Prerequisites
1.  **Python 3.x** installed.
2.  Install required libraries:
    ```bash
    pip install pynput pygame
    ```
3.  Place a file named `beep.wav` in the project folder.

### Gmail Configuration (Crucial)
Standard passwords will not work. You must:
1.  Enable **2-Step Verification** on your Google Account.
2.  Generate an **App Password** (labeled "Python Project").
3.  Paste that 16-character code into the `APP_PASSWORD` variable in the script.

### Execution via CMD
1.  Open Command Prompt and navigate to your folder:
    ```bash
    cd C:\Users\ADMIN\OneDrive\Documents\keylogger1
    ```
2.  Run the script:
    ```bash
    python keypython.py
    ```
3.  Press **ESC** to stop and save the logs.

---

## 📈 Future Enhancements
* **Desktop Screenshots:** Automatically take a photo of the screen when a trigger word is typed and attach it to the email.
* **Window Tracking:** Log which application was active (e.g., "Typed 'password' in Chrome").
* **Stealth Mode:** Convert the script to a `.exe` using PyInstaller and run it as a background process (`.pyw`).
* **Cloud Storage:** Upload the log file to a secure Dropbox or Google Drive folder every hour.

---

## ⚠️ Disadvantages & Limitations
* **Antivirus Flags:** Most modern Antivirus (like Windows Defender) will flag this script as a "Trojan" or "Spyware" because it captures keystrokes.
* **Plain Text Storage:** The `key_log.txt` file is not encrypted; anyone with access to the computer can read it.
* **Resource Usage:** If the log file becomes massive, it can slow down the system slightly if not cleared regularly.
* **Dependency on Internet:** If the computer is offline, the email notification will fail, though the local log will still save.

---

> **Disclaimer:** This project is for educational and authorized testing purposes only. Unauthorized use of this tool on a computer you do not own is strictly prohibited.
