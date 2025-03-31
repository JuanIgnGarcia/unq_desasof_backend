from sqlalchemy import Column, Integer, String
from src.service.database import Base

class Test(Base):
    __tablename__ = "test"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    numero = Column(Integer, nullable=False)
