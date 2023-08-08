from sqlalchemy.orm import sessionmaker
from .base import Base
from sqlalchemy import create_engine
import os

def get_db():
    engine = create_engine("postgresql+psycopg2://postgres:postgres@db:5432/assortdb")
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()