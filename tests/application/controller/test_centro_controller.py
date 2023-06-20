import pytest
from httpx import AsyncClient
from fastapi import status
import urllib.parse
from sqlalchemy import desc

GLOBAL_RESPONSE = []
HTTPS_CENTRO = "http://localhost:9092"

# CREATE
@pytest.mark.asyncio
async def test_create_centro():
    data = {        
        "descricao": "Criação de pastel",
        "data_agendada": "2023-01-01",
        "status": 2,
        "turno": 2,
        "id": 5
    }
    async with AsyncClient(base_url=HTTPS_CENTRO, timeout=50.0) as async_client:
        response = await async_client.post("/centro/", json=data)
    assert response.status_code == status.HTTP_201_CREATED

# GET ALL
@pytest.mark.asyncio
async def test_read_all_centro():
    async with AsyncClient(base_url=HTTPS_CENTRO, timeout=30.0) as async_client:
        response = await async_client.get("/centro/")
    assert response.status_code == status.HTTP_200_OK

# UPDATE
@pytest.mark.asyncio
async def test_update_centro():
    id = 5
    data = {        
        "descricao": "Criação de pastel e calda de cano",
        "data_agendada": "2023-01-01",
        "status": 1,
        "turno": 1,
        "id": 5
    }
    async with AsyncClient(base_url=HTTPS_CENTRO, timeout=50.0) as async_client:
        url = urllib.parse.urljoin("/centro/", str(id))
        response = await async_client.put(url, json=data)
    assert response.status_code == status.HTTP_201_CREATED

# DELETE
@pytest.mark.asyncio
async def test_delete_centro():
    id = 5

    async with AsyncClient(base_url=HTTPS_CENTRO, timeout=30.0) as async_client:
        url = urllib.parse.urljoin("/centro/", str(id))
        response = await async_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT