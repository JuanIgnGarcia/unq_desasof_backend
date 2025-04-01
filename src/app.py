from fastapi import FastAPI
from src.controllers.test_controller import router as test_router
from src.controllers.user_controller import router as user_router
from src.controllers.mercadolibre_controller import router as ml_router
from src.controllers.product_controller import router as product_router
from src.controllers.favorite_controller import router as favorite_router
from src.controllers.shopped_controller import router as shopped_router

from src.service.database import engine
from src.model.test import Base

app = FastAPI(
    title="UNQ-STC",
    description="",
)

Base.metadata.drop_all(bind=engine)  # elim las tablas existentes ---> Sacar en un futuro 
Base.metadata.create_all(bind=engine)  # crea las nuevas tablas

app.include_router(test_router, prefix="/test",tags=["Test"])
app.include_router(ml_router, prefix="/ml", tags=["MercadoLibre"])
app.include_router(user_router, prefix="/user",tags=["User"])
app.include_router(product_router, prefix="/product",tags=["Product"])
app.include_router(favorite_router,prefix="/favorites", tags=["favorites"])
app.include_router(shopped_router,prefix="/shopped", tags=["shopped"]) 

@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "ok"}

