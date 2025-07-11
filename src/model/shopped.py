from sqlalchemy import Column, Integer, Float, ForeignKey,String
from sqlalchemy.orm import relationship
from src.model.product import Product
from src.service.database import Base

class Shopped(Base):
    __tablename__ = "shopped"

    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users_buyer.id")) 

    product = relationship("Product", backref="shopped")
    user = relationship("UserBuyer", back_populates="shopped_items") 

    def __init__(self, amount: int, price: float, product_id: str):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        if price <= 0:
            raise ValueError("Price must be greater than 0")
        self.amount = amount
        self.price = price
        self.product_id = product_id
