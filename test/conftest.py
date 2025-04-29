import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from src.service.database import Base

from src.model.user_buyer import User,UserBuyer
from src.model.user_admin import UserAdmin
from src.model.shopped import  Shopped
from src.model.favorite import Favorite
from src.model.product import Product



#from sqlalchemy.ext.declarative import declarative_base
#Base = declarative_base()
DATABASE_URL = os.getenv("DATABASE_URL")

@pytest.fixture(scope="session")
def engine():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)

@pytest.fixture(scope="function")
def session(engine):
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#@pytest.fixture(autouse=True)
def clean_database(session):
    session.query(Shopped).delete()
    session.query(Favorite).delete()

    session.query(Product).delete()
    
    session.query(UserBuyer).delete()
    session.query(UserAdmin).delete()
    session.query(User).delete()
    session.commit()
    session.commit()

@pytest.fixture(autouse=True)
def reset_database(engine):
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)