from pydantic import BaseModel, Field
from typing import Optional

class FavoriteRequest(BaseModel):
    score: int = Field(..., ge=0, le=10)  # entre 0 y 10
    comment: str | None = None
    product_id: str
    product_title: str
    product_price: float
    product_currency: str
    product_url: Optional[str]

    class Config:
        from_attributes = True
