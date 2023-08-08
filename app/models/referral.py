from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from app.db.base_class import Base
import uuid
from sqlalchemy.dialects.postgresql import UUID

class Referral(Base):
    __tablename__ = "referrals"
    __table_args__ = {'schema': 'public'}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    referring_doctor = Column(String, nullable=False)
    patient_id = Column(UUID(as_uuid=True), ForeignKey('public.patients.id'))

    patient = relationship("Patient", back_populates="referrals")