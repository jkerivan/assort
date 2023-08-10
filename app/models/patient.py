from sqlalchemy import Column, String, Date
from app.db.base_class import Base
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

class Patient(Base):
    __tablename__ = 'patients'
    __table_args__ = {'schema': 'public'}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    address = Column(String)
    contact_number = Column(String)

    insurances = relationship("Insurance", back_populates="patient")
    referrals = relationship("Referral", back_populates="patient")
    appointments = relationship("Appointment", back_populates="patient")
    contact_information = relationship("ContactInformation", back_populates="patient") 