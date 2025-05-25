from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.service.product_service import ProductService
from src.service.database import get_db
from src.request.product_request import ProductRequest
from src.security.auth_dependencies import verify_token

router = APIRouter()

@router.post("/register", response_model=ProductRequest)
def create_product(product: ProductRequest, db: Session = Depends(get_db),username: str = Depends(verify_token)):
    service = ProductService(db)
    return service.save_product(product)

@router.get("/all", response_model=list[ProductRequest])
def get_products(db: Session = Depends(get_db)):
    service = ProductService(db)
    return service.get_all_products()
