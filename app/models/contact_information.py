

from sqlalchemy import Column, String
from sqlalchemy.sql.schema import ForeignKey
from app.db.base_class import Base
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

class ContactInformation(Base):
    __tablename__ = 'contact_information'
    __table_args__ = {'schema': 'public'}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    patient_id = Column(UUID(as_uuid=True), ForeignKey('public.patients.id'), unique=True, nullable=False)
    email = Column(String, unique=True, nullable=True)
    phone_number = Column(String, unique=True, nullable=True)
    address_id = Column(UUID(as_uuid=True), ForeignKey('public.addresses.id'), nullable=True)

    patient = relationship("Patient", back_populates="contact_information")
    address = relationship("Address")