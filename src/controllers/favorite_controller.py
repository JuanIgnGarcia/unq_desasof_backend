from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.service.database import get_db
from src.service.favorite_service import FavoriteService
from src.request.favorite_request import FavoriteRequest
from src.model.favorite import Favorite

router = APIRouter()

@router.get("/all", response_model=list[FavoriteRequest])
def get_all_favorites(db: Session = Depends(get_db)):
    service = FavoriteService(db)
    return service.get_all_favorites()
