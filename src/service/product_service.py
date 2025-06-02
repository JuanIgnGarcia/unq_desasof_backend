from sqlalchemy.orm import Session
from src.model.product import Product
from src.request.product_request import ProductRequest
from src.respond.product_response import ProductResponse 

class ProductService:
    def __init__(self, db: Session):
        self.db = db

    def create_product(self, product_request: ProductRequest) -> ProductResponse:
        existing_product = self.db.query(Product).filter_by(mercado_libre_id=product_request.id_ml).first()
        if existing_product:
            return existing_product

        new_product = Product(
            mercado_libre_id=product_request.id_ml,
            title=product_request.title,
            url=product_request.url,  
        )
        self.db.add(new_product)
        self.db.commit()
        self.db.refresh(new_product)
        return new_product

    def get_all_products(self):
        return self.db.query(Product).all()
