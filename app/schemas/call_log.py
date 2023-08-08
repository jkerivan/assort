from pydantic import BaseModel
from datetime import datetime

class CallLogBase(BaseModel):
    call_start_time: datetime
    call_end_time: datetime

class CallLogCreate(CallLogBase):
    pass

class CallLog(CallLogBase):
    id: int
    patient_id: int

    class Config:
        orm_mode = True
