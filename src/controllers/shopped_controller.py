from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.service.database import get_db
from src.service.shopped_service import ShoppedService
from src.request.shopped_request import ShoppedRequest

router = APIRouter()

@router.get("/all", response_model=list[ShoppedRequest])
def get_all_shopped(db: Session = Depends(get_db)):
    service = ShoppedService(db)
    return service.get_all_shopped()
