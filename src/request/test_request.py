from pydantic import BaseModel

class TestRequest(BaseModel):
    id: int
    nombre: str
    numero: int

    class Config:
        from_attributes = True 
