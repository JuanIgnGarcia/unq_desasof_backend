import httpx
from typing import Any, Dict
import asyncio
from config import BASE_URL,CLIENT_ID,CLIENT_SECRET,REFRESH_TOKEN

class MercadoLibreService:
    _access_token: str = ""

    async def _refresh_token(self) -> None:
        url = f"{BASE_URL}/oauth/token"
        data = {
            "grant_type": "refresh_token",
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "refresh_token": REFRESH_TOKEN,
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(url, data=data, headers={
                "accept": "application/json",
                "content-type": "application/x-www-form-urlencoded"
            })
            response.raise_for_status()
            self._access_token = response.json()["access_token"]
            print(f"Nuevo access_token: {self._access_token}")

    async def _get_headers(self) -> Dict[str, str]:
        if not self._access_token:
            await self._refresh_token()
        return {"Authorization": f"Bearer {self._access_token}"}

    async def get_item(self, item_id: str) -> Dict[str, Any]:
        url = f"{BASE_URL}/items/{item_id}"
        headers = await self._get_headers()
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers)
            if response.status_code == 401 or response.status_code == 403 :
                print("refresh token en get_item ")
                await self._refresh_token()
                headers = await self._get_headers()
                response = await client.get(url, headers=headers)
            response.raise_for_status()
            return response.json()


    async def search_items(self, query: str) -> Dict[str, Any]:
        url = f"{BASE_URL}/sites/MLA/search"
        params = {"q": query}
        headers = await self._get_headers()
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params, headers=headers)
            if response.status_code == 401 or response.status_code == 403 :
                await self._refresh_token()
                headers = await self._get_headers()
                response = await client.get(url, params=params, headers=headers)
            response.raise_for_status()
            return response.json()
