""" import pytest
from fastapi.testclient import TestClient
from src.application.controllers.CentroController import router_centro


client = TestClient(router_centro)


def test_create_centro():
    centro_data = {        
        "descricao": "Criação de pastel e caldo",
        "data_agendada": "2023-01-13",
        "status": 1,
        "turno": 2,
    }
   

    response = client.post("/centro/", json=centro_data)
    assert response.status_code == 201
    assert response.json() == centro_data


def test_get_all_centros():
    response = client.get("/centro/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# def test_update_centro():
#     centro_data = {        
#         "descricao": "Criação de pastel",
#         "data_agendada": "2023-01-02",
#         "status": 1,
#         "turno": 1,
#     }
#     response = client.post("/centro/", json=centro_data)
#     assert response.status_code == 201
#     centro_id = response.json()["id"]

#     updated_centro_data = {        
#         "descricao": "Criação de pastel e caldo de cano",
#         "data_agendada": "2023-01-02",
#         "status": 1,
#         "turno": 1,
#     }
#     response = client.put(f"/centro/{centro_id}", json=updated_centro_data)
#     assert response.status_code == 201

#     # Verifique se o centro foi atualizado corretamente
#     response = client.get(f"/centro/{centro_id}")
#     assert response.status_code == 200
#     assert response.json()["nome"] == updated_centro_data["nome"]


# def test_delete_centro():
#     centro_data = {        
#         "descricao": "Criação de pastel e caldo",
#         "data_agendada": "2023-01-01",
#         "status": 1,
#         "turno": 1,
#     }
#     response = client.post("/centro/", json=centro_data)
#     assert response.status_code == 201
#     centro_id = response.json()["id"]

#     response = client.delete(f"/centro/{centro_id}")
#     assert response.status_code == 204

#     response = client.get(f"/centro/{centro_id}")
#     assert response.status_code == 404

 """