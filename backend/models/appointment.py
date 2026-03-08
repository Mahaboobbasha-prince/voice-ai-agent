from sqlalchemy import Column, Integer, String
from backend.database.database import Base

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    patient_name = Column(String)
    doctor_name = Column(String)
    time_slot = Column(String)