from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.service.database import get_db
from src.service.shopped_service import ShoppedService
from src.respond.shopped_simple_response import ShoppedSimpleResponse
from src.security.auth_dependencies import verify_token

router = APIRouter()

@router.get("/all", response_model=list[ShoppedSimpleResponse])
def get_all_shopped(db: Session = Depends(get_db),username: str = Depends(verify_token)):
    service = ShoppedService(db)
    return service.get_all_shopped()
