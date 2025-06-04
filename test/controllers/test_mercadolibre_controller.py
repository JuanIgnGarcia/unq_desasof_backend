import pytest
from httpx import AsyncClient,HTTPError
from unittest.mock import AsyncMock, patch
from fastapi import FastAPI
from src.controllers.mercadolibre_controller import router

app = FastAPI()
app.include_router(router)

@pytest.mark.asyncio
async def test_search_ml_products_success():
    mock_response = {
        "query": "celular",
        "results": [
            {
                "id": "123",
                "name": "Celular XYZ",
                "date_created": "2023-01-01T00:00:00Z",
                "domain_id": "MLA-CELLPHONES",
                "pictures": [{"url": "https://image.com/img1.jpg"}]
            }
        ]
    }

    with patch("src.service.mercadolibre_service.MercadoLibreService.search_products", new=AsyncMock(return_value=mock_response)):
        async with AsyncClient(app=app, base_url="https://test") as ac:
            response = await ac.get("/search", params={"query": "celular"})

    assert response.status_code == 200
    assert response.json() == mock_response

@pytest.mark.asyncio
async def test_search_ml_products_failure():
    with patch(
    "src.service.mercadolibre_service.MercadoLibreService.search_products",
    new=AsyncMock(side_effect=HTTPError("falló"))
):
        async with AsyncClient(app=app, base_url="https://test") as ac:
            response = await ac.get("/search", params={"query": "celular"})

    assert response.status_code == 500
    assert "Error al consultar MercadoLibre" in response.json()["detail"]
