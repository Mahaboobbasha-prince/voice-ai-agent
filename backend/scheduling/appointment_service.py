# available_slots = {
#     "Dr Sharma": ["10:00", "11:00", "15:00"],
#     "Dr Patel": ["09:30", "14:00", "17:00"]
# }

appointments = []

doctor_slots = {
    "cardiologist": ["10:00", "11:00", "15:00"],
    "dermatologist": ["09:30", "13:00", "17:00"]
}

def check_availability(doctor):

    if doctor in doctor_slots:

        return doctor_slots[doctor]

    return []


def book_appointment(patient, doctor, time):

    for appt in appointments:
        if appt["doctor"] == doctor and appt["time"] == time:
            return "That slot is already booked."

    appointment = {
        "patient": patient,
        "doctor": doctor,
        "time": time
    }

    appointments.append(appointment)

    return f"Appointment confirmed with {doctor} at {time}"