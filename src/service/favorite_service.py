from sqlalchemy.orm import Session
from src.model.favorite import Favorite


class FavoriteService:
    def __init__(self, db: Session):
        self.db = db

    def get_all_favorites(self):
        return self.db.query(Favorite).all()
