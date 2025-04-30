import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from fastapi.testclient import TestClient
from src.service.database import Base,get_db
from src.app import app  

from src.model.user_buyer import User,UserBuyer
from src.model.user_admin import UserAdmin
from src.model.shopped import  Shopped
from src.model.favorite import Favorite
from src.model.product import Product


#from sqlalchemy.ext.declarative import declarative_base
#Base = declarative_base()
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://root:root@localhost:5432/testdb")

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

@pytest.fixture(autouse=True)
def reset_database(engine):
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

@pytest.fixture
def client(session):
    app.dependency_overrides[get_db] = lambda: session
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()