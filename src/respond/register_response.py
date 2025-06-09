from pydantic import BaseModel

class RegisterResponse(BaseModel):
    token: str