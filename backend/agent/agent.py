from dotenv import load_dotenv
import os
from backend.scheduling.appointment_service import check_availability, book_appointment
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key="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")

def process_user_input(user_input):

    if not user_input:
        return "I counldn't hear you clearly.Please try again."

    text = user_input.lower()

    if "available" in text or "availability" in text or "slot" in text or "time" in text:

        slots = check_availability("cardiologist")

        return f"Available slots are {slots}"

    elif "book" in text or "appointment" in text or "schedule" in text:

        return book_appointment("Patient", "cardiologist", "10:00")

    elif "cancel" in text:

        return "Your appointment has been cancelled."
    
    elif "stop" in text or "exit" in text:
        return "Stopping the Agent"

    # response = client.chat.completions.create(
    #     model="gpt-4o-mini",
    #     messages=[
    #         {"role": "system",
    #          "content": "You are a healthcare voice assistant that helps patients book appointments."},

    #         {"role": "user",
    #          "content": user_input}
    #     ]
    # )

    else:
        return "Sorry I didn't understand.Please say Book appointment or check availability."

