from pydantic import BaseModel

class TopProductResponse(BaseModel):
    id: str
    title: str
    url: str
    total_purchases: int
