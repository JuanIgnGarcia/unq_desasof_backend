import httpx
from typing import Any, Dict

BASE_URL = "https://api.mercadolibre.com"


HEADERS = {
    "Authorization": "Bearer TOKEN"  # modificar para que se recarge el token   
}


class MercadoLibreService:

    async def get_item(item_id: str) -> Dict[str, Any]:
        url = f"{BASE_URL}/items/{item_id}"
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=HEADERS)
            response.raise_for_status()
            return response.json()

    async def search_items(query: str) -> Dict[str, Any]:
        url = f"{BASE_URL}/sites/MLA/search"
        params = {"q": query}
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params, headers=HEADERS)
            response.raise_for_status()
            return response.json()

    async def get_all_items() -> Dict[str, Any]:
        url = f"{BASE_URL}/sites/MLA/search"
        params = {"q": "all"}
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            return response.json()