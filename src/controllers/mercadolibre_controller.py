from fastapi import APIRouter, HTTPException
import httpx
from src.service.mercadolibre_service import MercadoLibreService


router = APIRouter()

mercadolibre_service = MercadoLibreService()

@router.get("/items/{item_id}")
async def get_ml_item(item_id: str):
    try:
        item = await mercadolibre_service.get_item(item_id)
        return item
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/search")
async def search_ml_products(query: str):
    try:
        return await mercadolibre_service.search_products(query)
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"Error al consultar MercadoLibre: {str(e)}")
