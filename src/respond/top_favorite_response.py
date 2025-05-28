from pydantic import BaseModel

class TopFavoritesResponse(BaseModel):
    id: int
    title: str
    url: str
    total_favorites: int
