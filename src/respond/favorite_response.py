from pydantic import BaseModel
from typing import Optional

class FavoriteResponse(BaseModel):
    id: int
    score: int
    comment: Optional[str]
    product_id: int

    class Config:
        orm_mode = True
