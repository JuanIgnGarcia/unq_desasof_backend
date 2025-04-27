from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.service.database import get_db
from src.service.user_service import UserService
from src.request.user_request import UserAdminRequest, UserBuyerRequest,UserRequest
from src.request.favorite_request import FavoriteRequest
from src.request.shopped_request import ShoppedRequest
from src.respond.favorite_response import FavoriteResponse
from src.respond.shopped_response import ShoppedResponse


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

@router.get("/all", response_model=list[UserRequest])
def get_all_users(db: Session = Depends(get_db)):
    service.set_session(db)
    return service.get_all_users()

@router.get("/buyers", response_model=list[UserRequest])
def get_all_buyers(db: Session = Depends(get_db)):
    service.set_session(db)
    return service.get_all_buyers()

@router.post("/addFavorite/{user_id}", response_model=FavoriteResponse)
def add_favorite(user_id:int,favorite_request: FavoriteRequest, db: Session = Depends(get_db)):
    service.set_session(db)
    return service.add_favorite(user_id,favorite_request)

@router.get("/buyer/{buyer_id}", response_model=UserBuyerRequest)
def get_buyer(user_id:int,db: Session = Depends(get_db)):
    service.set_session(db)
    return service.get_buyers(user_id)

@router.post("/buy/{user_id}", response_model=ShoppedResponse)
def buy_product(user_id:int,shopped_request: ShoppedRequest, db: Session = Depends(get_db)):
    service.set_session(db)
    return service.buy_product(user_id,shopped_request)