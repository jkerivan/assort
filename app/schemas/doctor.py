from pydantic import BaseModel

class DoctorBase(BaseModel):
    name: str

class DoctorCreate(DoctorBase):
    pass

class Doctor(DoctorBase):
    id: int

    class Config:
        from_attributes = True
