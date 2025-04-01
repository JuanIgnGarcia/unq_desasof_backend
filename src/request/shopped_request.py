from pydantic import BaseModel, Field

class ShoppedRequest(BaseModel):
    amount: int = Field(..., gt=0)  
    price: float = Field(..., ge=0)  
    product_id: str 

    class Config:
        from_attributes = True
