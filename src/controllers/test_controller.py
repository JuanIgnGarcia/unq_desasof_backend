from fastapi import APIRouter

router = APIRouter(prefix="/test")

@router.get("/")
def get_test():
    return {"message": "Funciona"} 
