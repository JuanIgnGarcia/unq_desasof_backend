from fastapi import APIRouter, HTTPException
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
async def search_ml_items(query: str):
    try:
        results = await mercadolibre_service.search_items(query)
        return results
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/items")
async def all_items():
    try:
        items = await mercadolibre_service.get_all_items()
        return items
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=str(e))