from pydantic import BaseModel
from typing import List, Optional
from src.respond.favorite_response import FavoriteResponse
from src.respond.shopped_response import ShoppedResponse


class UserResponse(BaseModel):
    id: int
    username: str

class UserAdminResponse(UserResponse):
    pass  

class UserBuyerResponse(UserResponse):
    favorites: Optional[List[FavoriteResponse]] = []
    shopped_items: Optional[List[ShoppedResponse]] = []