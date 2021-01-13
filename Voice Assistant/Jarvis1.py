import pyttsx3
import speech_recognition as sr
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("good morning!")
    elif hour >= 12 and hour < 18:
        speak("good afternoon!")
    else:
        speak("good night!")
    speak("I am Jarvis my lord. What is your command?")

def takeCommand():
    # it takes microphone input from speaker and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("You can talk")
        print("Listening....")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        print("Done")

    try:
        print("Recognizing...")
        asked = r.recognize_google(audio,language='en-in')
        print(f"{asked}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"

    return asked

if __name__ == '__main__':
    takeCommand()