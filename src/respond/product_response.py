from pydantic import BaseModel
from typing import Optional

class ProductResponse(BaseModel):
    id: int
    id_ml: str
    title: str
    url: Optional[str]

    class Config:
        orm_mode = True