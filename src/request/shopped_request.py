from pydantic import BaseModel, Field
from typing import Optional

class ShoppedRequest(BaseModel):
    amount: int = Field(..., gt=0)  
    price: float = Field(..., ge=0)  
    product_id: int 
    product_id_ml: str
    product_title: str
    product_url: Optional[str]

    class Config:
        from_attributes = True
