from sqlalchemy.orm import Session
from src.model.test import Test

class TestService:
    def __init__(self, db: Session):
        self.db = db

    def get_all_tests(self):
        return self.db.query(Test).all()
