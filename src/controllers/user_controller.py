from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.service.database import get_db
from src.security.auth_dependencies import verify_token

from src.service.user_service import UserService
from src.request.favorite_request import FavoriteRequest
from src.request.shopped_request import ShoppedRequest
from src.request.login_request import LoginRequest

from src.respond.user_response import UserResponse,UserBuyerResponse
from src.respond.favorite_simple_response import FavoriteSimpleResponse
from src.respond.favorite_response import FavoriteResponse
from src.respond.shopped_response import ShoppedResponse
from src.respond.shopped_simple_response import ShoppedSimpleResponse
from src.respond.top_user_response import TopUserResponse
from src.respond.top_product_response import TopProductResponse
from src.respond.top_favorite_response import TopFavoritesResponse
from src.respond.register_response import RegisterResponse



router = APIRouter()

service = UserService(get_db)

# Login and registers 

@router.post("/login", response_model=RegisterResponse)
def login(request: LoginRequest, db: Session = Depends(get_db)):
    service.set_session(db)
    return service.login(request.username,request.password)

@router.post("/admin", response_model=RegisterResponse)
def create_admin(request: LoginRequest, db: Session = Depends(get_db)):
    service.set_session(db)
    return service.create_user_admin(request.username,request.password)

@router.post("/buyer", response_model=RegisterResponse)
def create_buyer(request: LoginRequest, db: Session = Depends(get_db)):
    service.set_session(db)
    return service.create_user_buyer(request.username,request.password)

@router.get("/all", response_model=list[UserResponse])
def get_all_users(db: Session = Depends(get_db), user_id: int = Depends(verify_token)):
    service.set_session(db)
    return service.get_all_users()

@router.get("/buyers", response_model=list[UserResponse])
def get_all_buyers(db: Session = Depends(get_db), user_id: int = Depends(verify_token)):
    service.set_session(db)
    return service.get_all_buyers()

@router.post("/addFavorite", response_model=FavoriteSimpleResponse)
def add_favorite(favorite_request: FavoriteRequest, db: Session = Depends(get_db),user_id: int = Depends(verify_token)):
    service.set_session(db)
    return service.add_favorite(user_id,favorite_request)

@router.post("/elimineFavorite")
def elimine_favorite(product_id_ml:str, db: Session = Depends(get_db),user_id: int = Depends(verify_token)):
    service.set_session(db)
    return service.elimine_favorite(user_id,product_id_ml)

@router.get("/buyer/me", response_model=UserBuyerResponse)
def get_buyer(db: Session = Depends(get_db),user_id: int = Depends(verify_token)):
    service.set_session(db)
    return service.get_buyers(user_id)

@router.post("/buy", response_model=ShoppedSimpleResponse)
def buy_product(shopped_request: ShoppedRequest, db: Session = Depends(get_db),user_id: int = Depends(verify_token)):
    service.set_session(db)
    return service.buy_product(user_id,shopped_request)

@router.get("/top5/users", response_model=list[TopUserResponse])
def top_5_users_with_most_purchases(db: Session = Depends(get_db),user_id: int = Depends(verify_token)):
    service.set_session(db)
    return service.top_5_users_with_most_purchases()

@router.get("/top5/shopped", response_model=list[TopProductResponse])
def top_5_most_shopped_product(db: Session = Depends(get_db),user_id: int = Depends(verify_token)):
    service.set_session(db)
    return service.top_5_most_shopped_product()

@router.get("/top5/favorites", response_model=list[TopFavoritesResponse])
def top_5_most_favorite_product(db: Session = Depends(get_db),user_id: int = Depends(verify_token)):
    service.set_session(db)
    return service.top_5_most_favorite_product()

@router.get("/favorite", response_model=list[FavoriteResponse])
def get_buyer_favorites(db: Session = Depends(get_db),user_id: int = Depends(verify_token)):
    service.set_session(db)
    return service.get_buyer_favorites(user_id)

@router.get("/shopped", response_model=list[ShoppedResponse])
def get_buyer_shopped( db: Session = Depends(get_db),user_id: int = Depends(verify_token)):
    service.set_session(db)
    return service.get_buyer_shopped(user_id)

@router.get("/isAdmin", response_model= bool)
def is_admin(db: Session = Depends(get_db),user_id: int = Depends(verify_token)):
    service.set_session(db)
    return service.is_admin(user_id)

@router.get("/isFavorite", response_model= bool)
def is_favorite(product_id_ml:str, db: Session = Depends(get_db),user_id: int = Depends(verify_token)):
    service.set_session(db)
    return service.is_favorite(user_id,product_id_ml)