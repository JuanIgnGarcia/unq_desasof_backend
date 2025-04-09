from pydantic import BaseModel, Field

class TopUserResponse(BaseModel):
    id: int
    username: str
    total_purchases: int
