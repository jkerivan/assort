from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base
import uuid
from sqlalchemy.dialects.postgresql import UUID

class Insurance(Base):
    __tablename__ = "insurances"
    __table_args__ = {'schema': 'public'}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    patient_id = Column(UUID(as_uuid=True), ForeignKey('public.patients.id'))

    payer = relationship("Payer", back_populates="insurances")
    patient = relationship("Patient", back_populates="insurances")
