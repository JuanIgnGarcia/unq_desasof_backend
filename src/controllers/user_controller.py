from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.service.database import get_db
from src.service.user_service import UserService
from src.request.user_request import UserAdminRequest, UserBuyerRequest,UserRequest
from src.request.favorite_request import FavoriteRequest
from src.respond.favorite_response import FavoriteResponse

router = APIRouter()

service = UserService(get_db)

@router.post("/admin", response_model=UserAdminRequest)
def create_admin(username: str, password: str, db: Session = Depends(get_db)):
    service.set_session(db)
    return service.create_user_admin(username,password)

@router.post("/buyer", response_model=UserBuyerRequest)
def create_buyer(username: str, password: str, db: Session = Depends(get_db)):
    service.set_session(db)
    return service.create_user_buyer(username,password)

@router.get("/", response_model=list[UserRequest])
def get_all_users(db: Session = Depends(get_db)):
    service.set_session(db)
    return service.get_all_users()

@router.post("/addFavorite/{user_id}", response_model=FavoriteResponse)
def add_favorite(user_id:int,favorite_request: FavoriteRequest, db: Session = Depends(get_db)):
    service.set_session(db)
    return service.add_favorite(user_id,favorite_request)
