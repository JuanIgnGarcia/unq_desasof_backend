from pydantic import BaseModel, Field
from typing import Optional

class LoginRequest(BaseModel):
    username: str
    password: str