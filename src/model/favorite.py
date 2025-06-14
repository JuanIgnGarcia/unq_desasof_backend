from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.service.database import Base

class Favorite(Base):
    __tablename__ = "favorites"

    id = Column(Integer, primary_key=True, autoincrement=True)
    score = Column(Integer, nullable=False)
    comment = Column(String, nullable=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users_buyer.id"))  
    
    product = relationship("Product", backref="favorites")
    user = relationship("UserBuyer", back_populates="favorites")  

    def __init__(self, score: int, comment: str | None, product_id: str):
        if not (0 <= score <= 10):
            raise ValueError("Score must be between 0 and 10")
        self.score = score
        self.comment = comment
        self.product_id = product_id
