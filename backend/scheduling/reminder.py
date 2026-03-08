from backend.scheduling.appointment_service import appointments

def send_reminders():

    for appt in appointments:

        print(f"Reminder: Appointment with {appt['doctor']} at {appt['time']}")