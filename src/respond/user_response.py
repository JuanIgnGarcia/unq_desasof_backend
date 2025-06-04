from pydantic import BaseModel
from typing import List, Optional
from src.respond.favorite_simple_response import FavoriteSimpleResponse
from src.respond.shopped_simple_response import ShoppedSimpleResponse


class UserResponse(BaseModel):
    id: int
    username: str

class UserAdminResponse(UserResponse):
    pass  

class UserBuyerResponse(UserResponse):
    favorites: Optional[List[FavoriteSimpleResponse]] = []
    shopped_items: Optional[List[ShoppedSimpleResponse]] = []