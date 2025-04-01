from pydantic import BaseModel, Field

class FavoriteRequest(BaseModel):
    score: int = Field(..., ge=0, le=10)  # entre 0 y 10
    comment: str | None = None
    product_id: str  
    
    class Config:
        from_attributes = True
