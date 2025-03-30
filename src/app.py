from fastapi import FastAPI
from src.controllers.test_controller import router as test_router

app = FastAPI(
    title="No-Conv-Grafos",
    description="",
)

app.include_router(test_router, prefix="/test", tags=["Process"])


@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "ok"}

