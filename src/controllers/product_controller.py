from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.service.product_service import ProductService
from src.service.database import get_db
from src.request.product_request import ProductRequest
from src.model.product import Product

router = APIRouter()

@router.post("/register", response_model=ProductRequest)
def create_product(product: ProductRequest, db: Session = Depends(get_db)):
    service = ProductService(db)
    return service.save_product(product)

@router.get("/all", response_model=list[ProductRequest])
def get_products(db: Session = Depends(get_db)):
    service = ProductService(db)
    return service.get_all_products()
