from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.service.database import get_db
from src.service.user_service import UserService
from src.request.user_request import UserAdminRequest, UserBuyerRequest
from src.request.user_request import UserRequest

router = APIRouter()

service = UserService(get_db)

@router.post("/admin", response_model=UserRequest)
def create_admin(user_request: UserAdminRequest, db: Session = Depends(get_db)):
    service.set_session(db)
    return service.create_user_admin(user_request)

@router.post("/buyer", response_model=UserRequest)
def create_buyer(user_request: UserBuyerRequest, db: Session = Depends(get_db)):
    service.set_session(db)
    return service.create_user_buyer(user_request)

@router.get("/", response_model=list[UserRequest])
def get_all_users(db: Session = Depends(get_db)):
    service.set_session(db)
    return service.get_all_users()
