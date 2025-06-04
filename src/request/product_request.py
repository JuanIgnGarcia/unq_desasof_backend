from pydantic import BaseModel

class ProductRequest(BaseModel):
    id_ml: str  
    title: str
    url: str | None = None  

    class Config:
        from_attributes = True
