from pydantic import BaseModel

class ProductRequest(BaseModel):
    id: str  
    title: str
    price: float
    currency: str
    url: str | None = None  

    class Config:
        from_attributes = True
