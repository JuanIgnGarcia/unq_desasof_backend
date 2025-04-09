from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.service.database import get_db
from src.service.shopped_service import ShoppedService
from src.respond.shopped_response import ShoppedResponse

router = APIRouter()

@router.get("/all", response_model=list[ShoppedResponse])
def get_all_shopped(db: Session = Depends(get_db)):
    service = ShoppedService(db)
    return service.get_all_shopped()
