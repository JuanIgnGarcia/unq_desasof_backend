from fastapi import FastAPI
from src.controllers import test_controller

app = FastAPI()

app.include_router(test_controller.router)

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI with Docker!"}
