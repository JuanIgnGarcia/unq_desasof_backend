from sqlalchemy.orm import Session
from src.model.shopped import Shopped
from src.request.shopped_request import ShoppedRequest

class ShoppedService:
    def __init__(self, db: Session):
        self.db = db

    def get_all_shopped(self):
        return self.db.query(Shopped).all()
