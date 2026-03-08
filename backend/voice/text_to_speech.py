from gtts import gTTS
import os
import time

def speak(text):

    print("Agent:", text)

    speech = gTTS(text)

    filename = f"response_{int(time.time())}.mp3"

    speech.save(filename)

    os.system(f"start {filename}")