from sqlalchemy.orm import Session
from src.model.user_admin import UserAdmin
from src.model.user_buyer import UserBuyer
from src.request.user_request import UserAdminRequest, UserBuyerRequest
from src.model.user import User

class UserService:
    def __init__(self, db: Session):
        self.db = db

    def create_user_admin(self, user_request: UserAdminRequest):
        user = UserAdmin(username=user_request.username, password=user_request.password)
        self.db.add(user)
        self.db.commit()
        return user

    def create_user_buyer(self, user_request: UserBuyerRequest):
        user = UserBuyer(username=user_request.username, password=user_request.password)
        self.db.add(user)
        self.db.commit()
        return user

    def get_all_users(self):
        return self.db.query(User).all()
