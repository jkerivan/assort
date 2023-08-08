from pydantic import BaseModel

class ContactInfoBase(BaseModel):
    phone_number: str
    email: str

class ContactInfoCreate(ContactInfoBase):
    pass

class ContactInfo(ContactInfoBase):
    id: int

    class Config:
        from_attributes = True