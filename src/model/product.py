from sqlalchemy import Column, Integer, String, Float
from src.service.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)  
    id_ml = Column(String, primary_key=True) # ID de ML
    title = Column(String, nullable=False)
    url = Column(String, nullable=True)  # URL de la imagen
