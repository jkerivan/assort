from pydantic import BaseModel
from datetime import datetime

class AppointmentBase(BaseModel):
    date_time: datetime
    doctor_id: int

class AppointmentCreate(AppointmentBase):
    pass

class Appointment(AppointmentBase):
    id: int

    class Config:
        orm_mode = True