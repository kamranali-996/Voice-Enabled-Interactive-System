import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import json
import os

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    try:
        print("🎤 Listening... Speak now!")
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
        command = recognizer.recognize_google(audio).lower()
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand that. Please try again.")
        return ""
    except sr.RequestError as e:
        speak(f"Speech recognition error: {e}")
        return ""
    except sr.WaitTimeoutError:
        return ""
    except Exception as e:
        speak("Microphone error. Please try again.")
        return ""

def load_contacts():
    contacts_file = "contacts.json"
    if os.path.exists(contacts_file):
        with open(contacts_file, 'r') as f:
            return json.load(f)
    else:
        return {
            "shweta": {"phone": "911234567890"},
            "kamran": {"phone": "919876543210"}
        }

def log_chat(action, details):
    log_file = "../logs/chat_logs.txt"
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(f"{timestamp} - {action}: {details}\n")

def send_whatsapp_message(contact_name, message):
    contacts = load_contacts()
    if contact_name.lower() in contacts:
        phone_number = contacts[contact_name.lower()]["phone"]
        
        now = datetime.datetime.now()
        hour = now.hour
        minute = (now.minute + 1) % 60
        if now.minute + 1 >= 60:
            hour = (hour + 1) % 24
            
        speak(f"Sending message to {contact_name}. Please ensure WhatsApp Web is open.")
        log_chat("MESSAGE_SENT", f"To: {contact_name}, Content: {message}")
        
        try:
            pywhatkit.sendwhatmsg(f"+{phone_number}", message, hour, minute, 15, True, 3)
            speak("Message sent successfully!")
        except Exception as e:
            speak(f"Failed to send message: {e}")
    else:
        speak(f"Contact {contact_name} not found in contacts.")

def read_last_message():
    log_file = "../logs/chat_logs.txt"
    if os.path.exists(log_file):
        with open(log_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            if lines:
                last_message = lines[-1].strip()
                speak(f"Your last message was: {last_message}")
            else:
                speak("No messages found in the log.")
    else:
        speak("No message log found.")

def main():
    speak("Voice Enabled Messaging System activated!")
    speak("How can I help you today?")
    
    contacts = load_contacts()
    
    while True:
        command = listen()
        
        if not command:
            continue
            
        if 'exit' in command or 'quit' in command or 'stop' in command:
            speak("Goodbye! Have a great day!")
            break
            
        elif 'send message to' in command:
            try:
                parts = command.split('send message to', 1)[1].strip()
                if 'say' in parts:
                    contact_name, message = parts.split('say', 1)
                    contact_name = contact_name.strip()
                    message = message.strip()
                else:
                    contact_name = parts
                    speak(f"What message would you like to send to {contact_name}?")
                    message = listen()
                    
                if message:
                    send_whatsapp_message(contact_name, message)
                
            except Exception as e:
                speak("Sorry, I couldn't process that request. Please try again.")
                print(f"Error: {e}")
                
        elif 'read my last message' in command or 'read last message' in command:
            read_last_message()
            
        elif 'list contacts' in command:
            contact_names = ", ".join(contacts.keys())
            speak(f"Your contacts are: {contact_names}")
            
        else:
            speak("Command not recognized. Try: 'send message to contact name' or 'read my last message'")

if __name__ == "__main__":
    main()