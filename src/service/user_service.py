from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from src.security.auth import create_access_token, verify_password,get_password_hash

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
from src.respond.top_product_response import TopProductResponse
from src.respond.top_favorite_response import TopFavoritesResponse
from src.respond.register_response import RegisterResponse

class UserService:
    def __init__(self, db: Session):
        self.db = db

    def set_session(self,db: Session):
        self.db = db

    def login(self,username: str, password: str): 
        user = self.db.query(User).filter(User.username == username).first()
        if not user or not verify_password(password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciales incorrectas",
            )
        
        token = create_access_token(data={"sub": user.username})
        return RegisterResponse(id=user.id,token=token)

    def create_user_admin(self, username: str, password: str):
        hashed_password = get_password_hash(password)
        user = UserAdmin(username=username, password=hashed_password)
        self.db.add(user)
        self.db.commit()
        token = create_access_token(data={"sub": user.username})
        return RegisterResponse(id=user.id,token=token)


    def create_user_buyer(self, username: str, password: str):
        hashed_password = get_password_hash(password)
        user = UserBuyer(username=username, password=hashed_password)
        self.db.add(user)
        self.db.commit()
        token = create_access_token(data={"sub": user.username})
        return RegisterResponse(id=user.id,token=token)

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
                id_ml=favorite_request.product_id_ml,
                title=favorite_request.product_title,                                                     
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
    

    def get_buyers(self,buyer_id:int):
        return self.db.query(UserBuyer).filter(UserBuyer.id == buyer_id).first()
    
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
                id_ml=shopped_request.product_id_ml,
                title=shopped_request.product_title,                                                      
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

    def top_5_most_shopped_product(self) -> list[TopProductResponse]:
        results = (
            self.db.query(
                Product.id,
                Product.title,
                Product.url,
                func.sum(Shopped.amount).label("total_purchases")
            )
            .join(Shopped, Product.id == Shopped.product_id)
            .group_by(Product.id)
            .order_by(desc("total_purchases"))
            .limit(5)
            .all()
        )

        return [
            TopProductResponse(
                id=product_id,
                title=title,
                url=url,
                total_purchases=total_purchases
            )
            for product_id, title, url, total_purchases in results
        ]

    def top_5_most_favorite_product(self) -> list[TopFavoritesResponse]:
        results = (
            self.db.query(
                Favorite.product_id.label("id"),
                Product.title,
                Product.url,
                func.count(Favorite.id).label("total_favorites")
            )
            .join(Product, Product.id == Favorite.product_id)
            .group_by(Favorite.product_id, Product.title, Product.url)
            .order_by(desc("total_favorites"))
            .limit(5)
            .all()
        )

        return [
            TopFavoritesResponse(
                id=row.id,
                title=row.title,
                url=row.url,
                total_favorites=row.total_favorites
            )
            for row in results
        ]