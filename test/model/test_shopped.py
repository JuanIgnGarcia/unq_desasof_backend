from src.model.shopped import  Shopped
from src.model.user_buyer import UserBuyer
from src.model.product import Product
import pytest

def test_create_shopped(session):
    product = Product(id_ml="ML123", title="Test Product")
    buyer = UserBuyer(username="buyeruser", password="password123", type="buyer")
    session.add_all([product, buyer])
    session.commit()

    shopped = Shopped(amount=2, price=150.0, product_id=product.id)
    shopped.user_id = buyer.id
    session.add(shopped)
    session.commit()

    retrieved_shopped = session.query(Shopped).first()
    assert retrieved_shopped is not None
    assert retrieved_shopped.amount == 2
    assert retrieved_shopped.price == 150.0
    assert retrieved_shopped.product.id == product.id
    assert retrieved_shopped.user.id == buyer.id

def test_create_shopped_invalid_amount(session):
    product = Product(id_ml="ML123", title="Test Product")
    buyer = UserBuyer(username="buyeruser", password="password123", type="buyer")
    session.add_all([product, buyer])
    session.commit()

    with pytest.raises(ValueError, match="Amount must be greater than 0"):
        Shopped(amount=0, price=150.0, product_id=product.id)


def test_create_shopped_invalid_price(session):
    product = Product(id_ml="ML123", title="Test Product")
    buyer = UserBuyer(username="buyeruser", password="password123", type="buyer")
    session.add_all([product, buyer])
    session.commit()

    with pytest.raises(ValueError, match="Price must be greater than 0"):
        Shopped(amount=2, price=0, product_id=product.id)        