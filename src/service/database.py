from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

#DATABASE_URL = "postgresql://root:root@db:5432/dbstc"
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://root:root@db:5432/dbstc")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

