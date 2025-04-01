from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.model.user import User

class UserAdmin(User):
    __tablename__ = "users_admin"
    
    id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    
    __mapper_args__ = {
        "polymorphic_identity": "admin"
    }
