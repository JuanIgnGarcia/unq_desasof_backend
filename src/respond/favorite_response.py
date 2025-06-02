from pydantic import BaseModel
from typing import Optional
from src.respond.product_response import ProductResponse 

class FavoriteResponse(BaseModel):  
    id: int
    score: int
    comment: Optional[str]
    product: ProductResponse 

    class Config:
        orm_mode = True