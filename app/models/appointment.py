from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship
from app.db.base_class import Base
import uuid
from sqlalchemy.dialects.postgresql import UUID

class Appointment(Base):
    __tablename__ = "appointments"
    __table_args__ = {'schema': 'public'}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    provider = Column(String, nullable=False)
    appointment_datetime = Column(DateTime)
    chief_complaint = Column(String)

    patient = relationship("Patient", back_populates="appointments")

    def __str__(self):
        return f"Appointment with {self.provider} on {self.appointment_datetime} - {self.chief_complaint}"