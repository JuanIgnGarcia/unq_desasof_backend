from src.model.user_buyer import UserBuyer
from src.model.user_admin import UserAdmin

def test_create_buyer(session):
    buyer = UserBuyer(username="buyeruser", password="password123", type="buyer")
    session.add(buyer)
    session.commit()

    retrieved_buyer = session.query(UserBuyer).filter_by(username="buyeruser").first()
    assert retrieved_buyer is not None
    assert retrieved_buyer.username == "buyeruser"
    assert isinstance(retrieved_buyer, UserBuyer)

def test_create_admin(session):
    admin = UserAdmin(username="adminuser", password="adminpass", type="admin")
    session.add(admin)
    session.commit()

    retrieved_admin = session.query(UserAdmin).filter_by(username="adminuser").first()
    assert retrieved_admin is not None
    assert retrieved_admin.username == "adminuser"
    assert isinstance(retrieved_admin, UserAdmin)    