import speech_recognition as sr

def transcribe():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("Speak now...")

        audio = recognizer.listen(source)

    try:

        text = recognizer.recognize_google(audio)

        print("User:", text)

        return text
    except:

        return ""