from src.model.user_buyer import UserBuyer
from src.model.shopped import Shopped
from src.model.product import Product
from src.model.favorite import Favorite

def test_create_admin(client):
    response = client.post("/user/admin", json={"username": "admin1", "password": "secure123"})
    assert response.status_code == 200
    data = response.json()
    assert "token" in data

def test_create_buyer(client):
    response = client.post("/user/buyer", json={"username": "buyer1", "password": "pass456"})
    assert response.status_code == 200
    data = response.json()
    assert "token" in data

def test_get_all_buyers(client):
    client.post("/user/buyer", json={"username": "buyer1", "password": "pass456"})
    register_response = client.post("/user/buyer", json={"username": "buyer2", "password": "pass789"})

    token = register_response.json()["token"]

    # Usar el token en el header Authorization
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/user/buyers", headers=headers)

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 2
    assert all("id" in buyer and "username" in buyer for buyer in data)

def test_add_favorite(client):
    create_response = client.post("/user/buyer", json={"username": "buyer1", "password": "pass456"})
    token = create_response.json()["token"]

    headers = {"Authorization": f"Bearer {token}"}

    example_favorite_request = {
        "score": 8,
        "comment": "Producto excelente",
        "product_id": 123,
        "product_id_ml": "MLA123",
        "product_title": "test",
        "product_url": "ULR_test"
    }
    response = client.post("/user/addFavorite", json=example_favorite_request,headers=headers)
    
    assert response.status_code == 200

    data = response.json()
    assert data["score"] == example_favorite_request["score"]
    assert data["comment"] == example_favorite_request["comment"]
    assert "product_id" in data

def test_get_buyer(client):
    create_response = client.post("/user/buyer", json={"username": "buyer1", "password": "pass456"})
    
    token = create_response.json()["token"]
    headers = {"Authorization": f"Bearer {token}"}

    response = client.get("/user/buyer/me",headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["username"] == "buyer1"
    assert "favorites" in data
    assert "shopped_items" in data

def test_buy_product(client):
    create_response = client.post("/user/buyer", json={"username": "buyer1", "password": "pass456"})
    
    token = create_response.json()["token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    example_shopped_request = {
        "amount": 2,
        "price": 150.75,
        "product_id": 123,
        "product_id_ml": "MLA123",
        "product_title": "test",
        "product_url": "ULR_test"
    }

    response = client.post("/user/buy", json=example_shopped_request,headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["amount"] == example_shopped_request["amount"]
    assert data["price"] == example_shopped_request["price"]
    assert "product_id" in data

def create_buyers_with_purchases(db):
    users = []
    shopped_data = [
        ("buyer0", 10),
        ("buyer1", 30),
        ("buyer2", 20),
        ("buyer3", 40),
        ("buyer4", 50),
        ("buyer5", 5),
    ]

    product = Product(title="Test Product",id_ml="MLA3",url="URL3")
    db.add(product)
    db.flush()

    for username, amount in shopped_data:
        buyer = UserBuyer(username=username, password="$2b$12$.d2RTkzYeK7oqi/C9Sa4Me86nT6oAvHf4TjDJ9nUCUT4sMEGiM7eG") #pass123
        db.add(buyer)
        db.flush() 

       
        shopped = Shopped(amount=amount, price=10, product_id=product.id)
        shopped.user = buyer  

        db.add(shopped)
        users.append(buyer)

    db.commit()
    return users


def test_top_5_users_with_most_purchases(client, session):
    create_buyers_with_purchases(session)

    login_response = client.post("/user/login", json={"username": "buyer1", "password": "pass123"})
    
    token = login_response.json()["token"]
    headers = {"Authorization": f"Bearer {token}"}

    response = client.get("/user/top5/users",headers=headers)
    assert response.status_code == 200

    data = response.json()

    assert len(data) == 5
    
    total_purchases_list = [user["total_purchases"] for user in data]
    expected_amounts = sorted([10, 30, 20, 40, 50, 5], reverse=True)[:5]
    assert total_purchases_list == expected_amounts

def create_products_with_shoppings(db):
    shopped_data = [
        ("Product A", 10),
        ("Product B", 30),
        ("Product C", 20),
        ("Product D", 40),
        ("Product E", 50),
        ("Product F", 5),
    ]

    buyer = UserBuyer(username="buyer_top", password="$2b$12$.d2RTkzYeK7oqi/C9Sa4Me86nT6oAvHf4TjDJ9nUCUT4sMEGiM7eG") #pass123
    db.add(buyer)
    db.flush()

    for i, (title, amount) in enumerate(shopped_data):
        product = Product(title=title, id_ml=f"MLA{i}", url=f"URL{i}")
        db.add(product)
        db.flush()

        shopped = Shopped(amount=amount, price=10, product_id=product.id)
        shopped.user = buyer  
        db.add(shopped)

    db.commit()


def test_top_5_most_shopped_product(client, session):
    create_products_with_shoppings(session)

    login_response = client.post("/user/login", json={"username": "buyer_top", "password": "pass123"})
    
    token = login_response.json()["token"]
    headers = {"Authorization": f"Bearer {token}"}

    response = client.get("/user/top5/shopped",headers=headers)
    assert response.status_code == 200
    data = response.json()

    assert len(data) == 5

    total_purchases_list = [product["total_purchases"] for product in data]
    expected_amounts = sorted([10, 30, 20, 40, 50, 5], reverse=True)[:5]
    assert total_purchases_list == expected_amounts

    for product in data:
        assert "id" in product
        assert "title" in product
        assert "url" in product
        assert "total_purchases" in product


def create_products_with_favorites(db):
    favorites_data = [
        ("Product A", 1),
        ("Product B", 3),
        ("Product C", 2),
        ("Product D", 4),
        ("Product E", 5),
        ("Product F", 0),
    ]

    buyer = UserBuyer(username="fav_buyer", password="$2b$12$.d2RTkzYeK7oqi/C9Sa4Me86nT6oAvHf4TjDJ9nUCUT4sMEGiM7eG") #pass123
    db.add(buyer)
    db.flush()

    for i, (title, fav_count) in enumerate(favorites_data):
        product = Product(title=title, id_ml=f"MLA-FAV-{i}", url=f"URL-FAV-{i}")
        db.add(product)
        db.flush()

        for j in range(fav_count):
            favorite = Favorite(score=8, comment=f"Nice {j}", product_id=product.id)
            favorite.user = buyer
            db.add(favorite)

    db.commit()


def test_top_5_most_favorite_product(client, session):
    create_products_with_favorites(session)

    login_response = client.post("/user/login", json={"username": "fav_buyer", "password": "pass123"})
    
    token = login_response.json()["token"]
    headers = {"Authorization": f"Bearer {token}"}

    response = client.get("/user/top5/favorites",headers=headers)
    assert response.status_code == 200
    data = response.json()

    assert len(data) == 5

    total_favorites_list = [product["total_favorites"] for product in data]
    expected_favorites = sorted([1, 3, 2, 4, 5, 0], reverse=True)[:5]
    assert total_favorites_list == expected_favorites

    for product in data:
        assert "id" in product
        assert "title" in product
        assert "url" in product
        assert "total_favorites" in product

def test_is_admin_buyer(client, session):
    create_response = client.post("/user/buyer", json={"username": "buyer1", "password": "pass456"})
    token = create_response.json()["token"]

    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/user/isAdmin",headers=headers)
    
    assert response.status_code == 200
    data = response.json()
    assert data == False

def test_is_admin_admin(client):
    create_response = client.post("/user/admin", json={"username": "admin1", "password": "pass456"})
    token = create_response.json()["token"]

    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/user/isAdmin",headers=headers)
    
    assert response.status_code == 200
    data = response.json()
    assert data == True

def test_get_buyer_shopped(client, session):
    create_products_with_shoppings(session)
    login_response = client.post("/user/login", json={"username": "buyer_top", "password": "pass123"})
    
    token = login_response.json()["token"]
    headers = {"Authorization": f"Bearer {token}"}

    response = client.get("/user/shopped",headers=headers)
    assert response.status_code == 200
    data = response.json()

    assert len(data) == 6
    for shopped in data:
        assert "amount" in shopped
        assert "price" in shopped
        assert "product_id" in shopped
        assert "product" in shopped

def test_get_buyer_favorites(client, session):
    create_products_with_favorites(session)
    login_response = client.post("/user/login", json={"username": "fav_buyer", "password": "pass123"})
    
    token = login_response.json()["token"]
    headers = {"Authorization": f"Bearer {token}"}

    response = client.get("/user/favorite",headers=headers)
    assert response.status_code == 200
    data = response.json()

    assert len(data) == 15
    for favorite in data:
        assert "id" in favorite
        assert "score" in favorite
        assert "comment" in favorite
        assert "product" in favorite

# TO DO :
#   - CREAR Admin con el mismo username 
#   - CREAR Buyer con el mismo username