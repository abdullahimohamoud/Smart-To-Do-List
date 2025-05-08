# voice_interface.py
# Copyright (c) 2025 made with love by @uncannystranger
import speech_recognition as sr
import pyttsx3

class VoiceInterface:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.tts_engine = pyttsx3.init()

    def listen(self):
        with sr.Microphone() as source:
            print("Listening for command...")
            audio = self.recognizer.listen(source)
        try:
            command = self.recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            self.speak("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            self.speak("Sorry, speech service is unavailable.")
            return None

    def speak(self, text):
        print(f"Assistant: {text}")
        self.tts_engine.say(text)
        self.tts_engine.runAndWait()
