from pydantic import BaseModel

class InsuranceBase(BaseModel):
    payer_name: str
    payer_id: str

class InsuranceCreate(InsuranceBase):
    pass

class Insurance(InsuranceBase):
    id: int

    class Config:
        orm_mode = True
