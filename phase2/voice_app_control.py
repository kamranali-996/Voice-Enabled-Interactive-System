import speech_recognition as sr
import pyttsx3
import json
import os
import subprocess
import psutil
import datetime
import webbrowser

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    print(f"Friday: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    try:
        print("🎤 Listening... Speak now!")
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=6)
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

def load_app_mapping():
    mapping_file = "apps_mapping.json"
    if os.path.exists(mapping_file):
        with open(mapping_file, 'r') as f:
            return json.load(f)
    else:
        return {
            "notepad": {"path": "notepad.exe", "process": "notepad.exe", "type": "app"},
            "calculator": {"path": "calc.exe", "process": "Calculator.exe", "type": "app"},
            "chrome": {"path": "chrome.exe", "process": "chrome.exe", "type": "app"},
            "paint": {"path": "mspaint.exe", "process": "mspaint.exe", "type": "app"},
            "youtube": {"url": "https://www.youtube.com", "type": "website"},
            "google": {"url": "https://www.google.com", "type": "website"},
            "gmail": {"url": "https://www.gmail.com", "type": "website"},
            "whatsapp": {"url": "https://web.whatsapp.com", "type": "website"},
            "facebook": {"url": "https://www.facebook.com", "type": "website"},
            "instagram": {"url": "https://www.instagram.com", "type": "website"}
        }

def log_action(action, app_name):
    log_file = "../logs/app_logs.txt"
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(f"{timestamp} - {action}: {app_name}\n")

def open_application(app_name):
    mapping = load_app_mapping()
    if app_name in mapping:
        app_info = mapping[app_name]
        
        if app_info.get("type") == "website":
            # Open website in browser
            url = app_info["url"]
            webbrowser.open(url)
            speak(f"Opening {app_name} in your browser")
            log_action("WEBSITE_OPENED", f"{app_name} ({url})")
            
        else:
            # Open regular application
            app_path = app_info["path"]
            try:
                subprocess.Popen(app_path)
                speak(f"Opening {app_name}")
                log_action("APP_OPENED", app_name)
            except Exception as e:
                speak(f"Sorry, I couldn't open {app_name}")
                print(f"Error: {e}")
    else:
        speak(f"Application {app_name} is not configured.")
        speak("Say 'list apps' to see available applications.")

def close_application(app_name):
    mapping = load_app_mapping()
    if app_name in mapping:
        app_info = mapping[app_name]
        
        if app_info.get("type") == "website":
            speak("I cannot close websites automatically. Please close the browser tab manually.")
        else:
            process_name = app_info["process"]
            try:
                closed = False
                for proc in psutil.process_iter(['name']):
                    if proc.info['name'].lower() == process_name.lower():
                        proc.terminate()
                        closed = True
                        
                if closed:
                    speak(f"Closing {app_name}")
                    log_action("APP_CLOSED", app_name)
                else:
                    speak(f"{app_name} is not currently running.")
                    
            except Exception as e:
                speak(f"Sorry, I couldn't close {app_name}")
    else:
        speak(f"Application {app_name} is not configured.")

def main():
    speak("Hello I am Friday , how can i help you Today ?")
    
    mapping = load_app_mapping()
    app_names = ", ".join(mapping.keys())
    speak(f"Available applications and websites: {app_names}")
    
    while True:
        command = listen()
        
        if not command:
            continue
            
        if 'exit' in command or 'quit' in command or 'stop' in command:
            speak("Goodbye!")
            break
            
        elif command.startswith('open '):
            app_name = command.replace('open ', '').strip()
            open_application(app_name)
            
        elif command.startswith('close '):
            app_name = command.replace('close ', '').strip()
            close_application(app_name)
            
        elif command.startswith('start '):
            app_name = command.replace('start ', '').strip()
            open_application(app_name)
            
        elif 'list apps' in command:
            speak(f"Available: {app_names}")
            
        else:
            speak("Command not recognized. Try 'open notepad' or 'close calculator'")

if __name__ == "__main__":
    main()