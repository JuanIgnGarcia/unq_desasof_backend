from pydantic import BaseModel
from typing import Optional

class FavoriteSimpleResponse(BaseModel):  #FavoriteSimpleResponse
    id: int
    score: int
    comment: Optional[str]
    product_id: int

    class Config:
        orm_mode = True
