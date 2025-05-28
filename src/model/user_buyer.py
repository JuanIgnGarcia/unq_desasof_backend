from sqlalchemy import ForeignKey,Column,Integer
from sqlalchemy.orm import relationship
from src.model.user import User

class UserBuyer(User):
    __tablename__ = "users_buyer"
    
    id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    
    favorites = relationship("Favorite", back_populates="user", cascade="all, delete-orphan") 
    shopped_items = relationship("Shopped", back_populates="user", cascade="all, delete-orphan")  

    __mapper_args__ = {
        "polymorphic_identity": "buyer"
    }
