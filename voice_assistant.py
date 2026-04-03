import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import random
import pyautogui
import pyjokes
import subprocess

# ================= ENGINE SETUP =================
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

# ================= SPEAK =================
def speak(text):
    engine.say(text)
    engine.runAndWait()

# ================= TIME & DATE =================
def tell_time():
    now = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {now}")
    print(now)

def tell_date():
    now = datetime.datetime.now()
    speak(f"Today is {now.day} {now.strftime('%B')} {now.year}")
    print(now)

# ================= WISH =================
def wishme():
    hour = datetime.datetime.now().hour

    if 4 <= hour < 12:
        speak("Good morning")
    elif 12 <= hour < 16:
        speak("Good afternoon")
    else:
        speak("Good evening")

    name = load_name()
    speak(f"{name} ready")

# ================= NAME =================
def set_name():
    speak("What should I be called?")
    name = takecommand()
    if name:
        with open("assistant_name.txt", "w") as f:
            f.write(name)
        speak(f"My name is now {name}")

def load_name():
    try:
        with open("assistant_name.txt", "r") as f:
            return f.read().strip()
    except:
        return "Jarvis"

# ================= COMMAND =================
def takecommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1

        try:
            audio = r.listen(source, timeout=5)
        except sr.WaitTimeoutError:
            return None

    try:
        query = r.recognize_google(audio, language="en-US")
        print("You said:", query)
        return query.lower()
    except:
        return None

# ================= MUSIC =================
def play_music(song_name=None):
    music_dir = os.path.join(os.path.expanduser("~"), "Music")

    if not os.path.exists(music_dir):
        speak("Music folder not found")
        return

    songs = os.listdir(music_dir)

    if song_name:
        songs = [s for s in songs if song_name in s.lower()]

    if songs:
        song = random.choice(songs)
        path = os.path.join(music_dir, song)

        try:
            os.startfile(path)  # Windows
        except:
            subprocess.call(["xdg-open", path])  # Linux

        speak(f"Playing {song}")
    else:
        speak("No song found")

# ================= SCREENSHOT =================
def screenshot():
    filename = f"screenshot_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    path = os.path.join(os.path.expanduser("~"), "Pictures", filename)

    img = pyautogui.screenshot()
    img.save(path)

    speak("Screenshot saved")
    print(path)

# ================= WIKIPEDIA =================
def search_wikipedia(query):
    try:
        result = wikipedia.summary(query, sentences=2)
        speak(result)
        print(result)
    except:
        speak("No result found")

# ================= GOOGLE SEARCH =================
def search_google(query):
    url = f"https://www.google.com/search?q={query}"
    wb.open(url)
    speak("Searching Google")

# ================= SAFE POWER =================
def confirm_action(action):
    speak(f"Are you sure you want to {action}?")
    ans = takecommand()
    return ans and "yes" in ans

# ================= MAIN =================
if __name__ == "__main__":
    wishme()

    while True:
        query = takecommand()

        if query is None:
            continue

        # Wake word
        if "jarvis" not in query:
            continue

        query = query.replace("jarvis", "").strip()

        if "time" in query:
            tell_time()

        elif "date" in query:
            tell_date()

        elif "wikipedia" in query:
            search_wikipedia(query.replace("wikipedia", ""))

        elif "play music" in query:
            play_music(query.replace("play music", ""))

        elif "open youtube" in query:
            wb.open("https://youtube.com")

        elif "open google" in query:
            wb.open("https://google.com")

        elif "search" in query:
            search_google(query.replace("search", ""))

        elif "change name" in query:
            set_name()

        elif "screenshot" in query:
            screenshot()

        elif "joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)
            print(joke)

        elif "shutdown" in query:
            if confirm_action("shutdown"):
                os.system("shutdown /s /f /t 1")
                break

        elif "restart" in query:
            if confirm_action("restart"):
                os.system("shutdown /r /f /t 1")
                break

        elif "exit" in query:
            speak("Goodbye")
            break