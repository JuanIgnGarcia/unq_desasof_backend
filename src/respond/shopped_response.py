from pydantic import BaseModel, Field

class ShoppedResponse(BaseModel):
    amount: int = Field(..., gt=0)  
    price: float = Field(..., ge=0)  
    product_id: int 

    class Config:
        from_attributes = True
