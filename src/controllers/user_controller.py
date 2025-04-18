from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.service.database import get_db
from src.service.user_service import UserService
from src.request.favorite_request import FavoriteRequest
from src.request.shopped_request import ShoppedRequest
from src.respond.user_response import UserResponse,UserAdminResponse,UserBuyerResponse
from src.respond.favorite_response import FavoriteResponse
from src.respond.shopped_response import ShoppedResponse
from src.respond.top_user_response import TopUserResponse
from src.respond.top_product_response import TopProductResponse

router = APIRouter()

service = UserService(get_db)

@router.post("/admin", response_model=UserAdminResponse)
def create_admin(username: str, password: str, db: Session = Depends(get_db)):
    service.set_session(db)
    return service.create_user_admin(username,password)

@router.post("/buyer", response_model=UserBuyerResponse)
def create_buyer(username: str, password: str, db: Session = Depends(get_db)):
    service.set_session(db)
    return service.create_user_buyer(username,password)

@router.get("/all", response_model=list[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    service.set_session(db)
    return service.get_all_users()

@router.get("/buyers", response_model=list[UserResponse])
def get_all_buyers(db: Session = Depends(get_db)):
    service.set_session(db)
    return service.get_all_buyers()

@router.post("/addFavorite/{user_id}", response_model=FavoriteResponse)
def add_favorite(user_id:int,favorite_request: FavoriteRequest, db: Session = Depends(get_db)):
    service.set_session(db)
    return service.add_favorite(user_id,favorite_request)

@router.get("/buyer/{buyer_id}", response_model=UserBuyerResponse)
def get_buyer(user_id:int,db: Session = Depends(get_db)):
    service.set_session(db)
    return service.get_buyers(user_id)

@router.post("/buy/{user_id}", response_model=ShoppedResponse)
def buy_product(user_id:int,shopped_request: ShoppedRequest, db: Session = Depends(get_db)):
    service.set_session(db)
    return service.buy_product(user_id,shopped_request)

@router.get("/top5/users", response_model=list[TopUserResponse])
def top_5_users_with_most_purchases(db: Session = Depends(get_db)):
    service.set_session(db)
    return service.top_5_users_with_most_purchases()

@router.get("/top5/shopped", response_model=list[TopProductResponse])
def top_5_most_shopped_product(db: Session = Depends(get_db)):
    service.set_session(db)
    return service.top_5_most_shopped_product()