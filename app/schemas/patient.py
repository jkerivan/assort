from pydantic import BaseModel

class PatientBase(BaseModel):
    name: str
    date_of_birth: str

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    id: int

    class Config:
        from_attributes = True
