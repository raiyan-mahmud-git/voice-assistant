# Voice Assistant (Jarvis) - Python Project

# Description

This is a Python-based voice assistant that can perform basic tasks using voice commands. It uses speech recognition to understand user input and text-to-speech to respond. The assistant can tell the time and date, search Wikipedia, open websites, play music, take screenshots, tell jokes, and perform basic system operations.


Features

- Voice command recognition
- Text-to-speech response
- Wake word activation ("Jarvis")
- Tell current time and date
- Search Wikipedia
- Google search fallback
- Play music from local storage
- Open websites (YouTube, Google)
- Take screenshots with timestamp
- Tell jokes
- Change assistant name
- Safe shutdown and restart with confirmation


# Technologies Used

- Python
- pyttsx3 (text-to-speech)
- SpeechRecognition (voice input)
- Wikipedia API
- pyautogui (automation)
- pyjokes


# Installation

1. Clone the repository or download the code
2. Install required libraries:

pip install pyttsx3 SpeechRecognition wikipedia pyautogui pyjokes pyaudio

3. Run the script:

python main.py


# Usage

- Start the program
- Speak commands starting with the wake word "Jarvis"
- Example commands:
  - "Jarvis what is the time"
  - "Jarvis search Python programming"
  - "Jarvis play music"
  - "Jarvis take a screenshot"
  - "Jarvis tell me a joke"


# Notes

- Microphone access is required
- Music will play from your system's default Music folder
- Screenshot will be saved in the Pictures folder
- Some features (shutdown/restart) work best on Windows


# Limitations

- Requires internet for speech recognition and Wikipedia
- Limited natural language understanding
- No GUI (runs in terminal)
- Wake word detection is basic (not always accurate)


# Future Improvements

- Add graphical user interface (GUI)
- Integrate AI (ChatGPT API)
- Add task automation (open apps, reminders, etc.)
- Improve wake word detection
- Make fully cross-platform


# License

This project is for educational and personal use.
