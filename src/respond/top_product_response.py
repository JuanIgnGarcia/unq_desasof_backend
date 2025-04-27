from pydantic import BaseModel

class TopProductResponse(BaseModel):
    id: int
    title: str
    url: str
    total_purchases: int
