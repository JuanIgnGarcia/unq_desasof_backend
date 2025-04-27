from fastapi import HTTPException, status
from sqlalchemy import func, desc
from sqlalchemy.orm import Session
from src.model.user_admin import UserAdmin
from src.model.user_buyer import UserBuyer
from src.model.user import User
from src.model.favorite import Favorite
from src.model.product import Product
from src.model.shopped import Shopped
from src.request.favorite_request import FavoriteRequest
from src.request.shopped_request import ShoppedRequest
from src.respond.favorite_response import FavoriteResponse
from src.respond.top_user_response import TopUserResponse

class UserService:
    def __init__(self, db: Session):
        self.db = db

    def set_session(self,db: Session):
        self.db = db

    def create_user_admin(self, username: str, password: str):
        user = UserAdmin(username=username, password=password)
        self.db.add(user)
        self.db.commit()
        return user

    def create_user_buyer(self, username: str, password: str):
        user = UserBuyer(username=username, password=password)
        self.db.add(user)
        self.db.commit()
        return user

    def get_all_users(self):
        return self.db.query(User).all()
    
    def get_all_buyers(self):
        return self.db.query(UserBuyer).all()

    def add_favorite(self, user_id: int, favorite_request: FavoriteRequest):
        user = self.db.query(UserBuyer).filter(UserBuyer.id == user_id).first()
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"UserBuyer with id {user_id} not found"
            )

        product = self.db.query(Product).filter(Product.id == favorite_request.product_id).first()
        if product is None:
            product = Product(
                id=favorite_request.product_id,
                title=favorite_request.product_title,                                  
                price=favorite_request.product_price,                                   
                currency=favorite_request.product_currency,                       
                url=favorite_request.product_url
            )
            self.db.add(product)
            self.db.commit()
            self.db.refresh(product)

        new_favorite = Favorite(
            score=favorite_request.score,
            comment=favorite_request.comment,
            product_id=product.id
        )
        user.favorites.append(new_favorite)
        self.db.add(new_favorite)
        self.db.commit()
        self.db.refresh(new_favorite)

        favorite_response = FavoriteResponse(
            id=new_favorite.id,
            score=new_favorite.score,
            comment=new_favorite.comment,
            product_id=product.id,
        )

        return favorite_response
    

    def get_buyers(self,user_id:int):
        return self.db.query(UserBuyer).filter(UserBuyer.id == user_id).first()
    
    def buy_product(self, user_id: int, shopped_request: ShoppedRequest):
        user = self.db.query(UserBuyer).filter(UserBuyer.id == user_id).first()
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"UserBuyer with id {user_id} not found"
            )

        product = self.db.query(Product).filter(Product.id == shopped_request.product_id).first()
        if product is None:
            product = Product(
                id=shopped_request.product_id,
                title=shopped_request.product_title,                                  
                price=shopped_request.product_price,                                   
                currency=shopped_request.product_currency,                       
                url=shopped_request.product_url
            )
            self.db.add(product)
            self.db.commit()
            self.db.refresh(product)

        shopped = Shopped(amount=shopped_request.amount,
                          price=shopped_request.price,
                          product_id=shopped_request.product_id)
        
        user.shopped_items.append(shopped)
        self.db.add(shopped)
        self.db.commit()
        self.db.refresh(shopped)

        return shopped_request

    def top_5_users_with_most_purchases(self) -> list[TopUserResponse]:
        results = (
            self.db.query(
                User.id,
                User.username,
                func.sum(Shopped.amount).label("total_purchases")
            )
            .join(Shopped, User.id == Shopped.user_id)
            .group_by(User.id)
            .order_by(desc("total_purchases"))
            .limit(5)
            .all()
        )

        return [
            TopUserResponse(
                id=user_id,
                username=username,
                total_purchases=total_purchases
            )
            for user_id, username, total_purchases in results
        ]
