from sqlalchemy import Column, Integer, String
from src.service.database import Base


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    type = Column(String, nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": "user",
        "polymorphic_on": type
    }
