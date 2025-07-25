from pydantic import BaseModel, Field
from src.respond.product_response import ProductResponse 

class ShoppedResponse(BaseModel):  
    amount: int = Field(..., gt=0)  
    price: float = Field(..., ge=0)  
    product_id: int 
    product: ProductResponse 

    class Config:
        orm_mode = True