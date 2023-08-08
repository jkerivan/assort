from .patient import Patient
from typing import List
from .call_log import CallLog

class PatientCallLog(Patient):
    call_logs: List[CallLog] = []

    class Config:
        from_attributes = True