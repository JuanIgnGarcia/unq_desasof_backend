from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.service.test_service import TestService
from src.service.database import get_db
from src.request.test_request import TestRequest

router = APIRouter()

@router.get("/all", response_model=list[TestRequest])
def get_tests(db: Session = Depends(get_db)):
    service = TestService(db)
    return service.get_all_tests()

@router.get("/")
def get_test():
    return {"message": "Funciona"} 
