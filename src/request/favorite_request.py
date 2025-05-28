from pydantic import BaseModel, Field
from typing import Optional

class FavoriteRequest(BaseModel):
    score: int = Field(..., ge=0, le=10)  # entre 0 y 10
    comment: str | None = None
    product_id: int
    product_id_ml: str
    product_title: str
    product_url: Optional[str]

    class Config:
        from_attributes = True
