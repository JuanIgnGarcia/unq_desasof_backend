from src.model.favorite import  Favorite
from src.model.user_buyer import UserBuyer
from src.model.product import Product
import pytest

def test_create_favorite(session):
    product = Product(id_ml="ML123", title="Test Product")
    buyer = UserBuyer(username="buyeruser", password="password123", type="buyer")
    session.add_all([product, buyer])
    session.commit()

    favorite = Favorite(score=8, comment="Great product!", product_id=product.id)
    favorite.user_id = buyer.id
    session.add(favorite)
    session.commit()

    retrieved_favorite = session.query(Favorite).first()
    assert retrieved_favorite is not None
    assert retrieved_favorite.score == 8
    assert retrieved_favorite.comment == "Great product!"
    assert retrieved_favorite.product.id == product.id
    assert retrieved_favorite.user.id == buyer.id

def test_create_favorite_invalid_score(session):
    product = Product(id_ml="ML123", title="Test Product")
    buyer = UserBuyer(username="buyeruser", password="password123", type="buyer")
    session.add_all([product, buyer])
    session.commit()

    with pytest.raises(ValueError, match="Score must be between 0 and 10"):
        Favorite(score=15, comment="Too good", product_id=product.id)