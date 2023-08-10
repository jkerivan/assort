from sqlalchemy.orm import sessionmaker
from .base import Base
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
load_dotenv()


def get_db():
    engine = create_engine(os.environ.get("DATABASE_URL", ""))
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()