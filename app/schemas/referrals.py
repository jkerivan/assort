from pydantic import BaseModel

class ReferralBase(BaseModel):
    referred_to: str

class ReferralCreate(ReferralBase):
    pass

class Referral(ReferralBase):
    id: int

    class Config:
        from_attributes = True