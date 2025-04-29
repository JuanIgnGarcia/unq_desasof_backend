from src.model.product import Product

def test_create_product(session):
    product = Product(id_ml="ML123", title="Product title", url="URL1")
    session.add(product)
    session.commit()

    retrieved_product = session.query(Product).filter_by(id_ml="ML123").first()
    assert retrieved_product is not None
    assert retrieved_product.title == "Product title"
    assert retrieved_product.url == "URL1"