from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.controllers.user_controller import router as user_router
from src.controllers.mercadolibre_controller import router as ml_router
from src.controllers.product_controller import router as product_router
from src.controllers.favorite_controller import router as favorite_router
from src.controllers.shopped_controller import router as shopped_router
from prometheus_fastapi_instrumentator import Instrumentator

from src.service.database import engine,Base

app = FastAPI(
    title="UNQ-STC",
    description="",
)

Instrumentator().instrument(app).expose(app)

#Base.metadata.drop_all(bind=engine)  # elim las tablas existentes ---> Sacar en un futuro 
#Base.metadata.create_all(bind=engine)  # crea las nuevas tablas

app.include_router(ml_router, prefix="/ml", tags=["MercadoLibre"])
app.include_router(user_router, prefix="/user",tags=["User"])
app.include_router(product_router, prefix="/product",tags=["Product"])
app.include_router(favorite_router,prefix="/favorites", tags=["favorites"])
app.include_router(shopped_router,prefix="/shopped", tags=["shopped"]) 


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ajusta para producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "ok"}

