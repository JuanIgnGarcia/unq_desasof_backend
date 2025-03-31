from fastapi import FastAPI
from src.controllers.test_controller import router as test_router
#from src.controllers.user_controller import router as user_router
from src.controllers.mercadolibre_controller import router as ml_router

app = FastAPI(
    title="No-Conv-Grafos",
    description="",
)

app.include_router(test_router, prefix="/test")
#app.include_router(user_router, prefix="/user")
app.include_router(ml_router, prefix="/ml", tags=["MercadoLibre"])

@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "ok"}

