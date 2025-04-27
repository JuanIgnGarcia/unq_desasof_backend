from sqlalchemy import Integer
from pydantic import BaseModel
from typing import List, Optional
from src.request.favorite_request import FavoriteRequest
from src.request.shopped_request import ShoppedRequest

class UserRequest(BaseModel):
    id: int
    username: str
    password: str

class UserAdminRequest(UserRequest):
    pass  

class UserBuyerRequest(UserRequest):
    favorites: Optional[List[FavoriteRequest]] = []
    shopped_items: Optional[List[ShoppedRequest]] = []