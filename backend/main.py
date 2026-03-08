from backend.voice.speech_to_text import transcribe
from backend.voice.text_to_speech import speak
from backend.agent.agent import process_user_input
import time

def run_voice_agent():

    print("Voice AI Agent Started")

    while True:

        start = time.time()

        user_text = transcribe()

        response = process_user_input(user_text)

        speak(response)

        latency = time.time() - start

        with open("logs/latency.log", "a") as f:
            f.write(f"{latency}\n")

        print("Latency:", latency)


if __name__ == "__main__":
    run_voice_agent()