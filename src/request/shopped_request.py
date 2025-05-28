from pydantic import BaseModel, Field
from typing import Optional

class ShoppedRequest(BaseModel):
    amount: int = Field(..., gt=0)  
    price: float = Field(..., ge=0)  
    product_id: str 
    product_id_ml:int
    product_title: str
    product_url: Optional[str]

    class Config:
        from_attributes = True
