from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.service.database import get_db
from src.service.favorite_service import FavoriteService
from src.respond.favorite_response import FavoriteResponse

router = APIRouter()

@router.get("/all", response_model=list[FavoriteResponse])
def get_all_favorites(db: Session = Depends(get_db)):
    service = FavoriteService(db)
    return service.get_all_favorites()
