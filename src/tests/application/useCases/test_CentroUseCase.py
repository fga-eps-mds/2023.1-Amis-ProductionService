from application.useCases.CentroUseCase import CentroUseCase
from infrastructure.repositories.CentroRepository import CentroRepository
from infrastructure.repositories.CentroInscricoesRepository import CentroInscricoesRepository
from domain.entities.Centro import Centro, CentroResponse, CentroRequest
from unittest.mock import MagicMock
import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from typing import NoReturn

test_session = UnifiedAlchemyMagicMock

def get_mock_db_session():
    return test_session

centro_repo = CentroRepository(session = get_mock_db_session())
centro_inscricoes = CentroInscricoesRepository(session=get_mock_db_session())
centro_use_Case = CentroUseCase(
    centroRepository=centro_repo,
    centroInscricoesRepository = centro_inscricoes,
)

test_listCentro= [ 
    (Centro (
    descricao= "Centro produtivo de teste 2/3",
       data_agendada= "2023-07-08",
       status= 1,
       turno= 1,
       vagas= 21,
       id= 2,
       )),
    (Centro(
        descricao= "Centro produtivo de teste",
        data_agendada= "2023-07-07",
        status= 1,
        turno= 2,
        vagas= 28,
        id= 3 
    )),
] 

@pytest.mark.parametrize(
    "centroSent",
    test_listCentro,
)

def test_save_centro(centroSent):
    response = centro_use_Case.save(centroSent= centroSent)
    assert centroSent == response, response.__dict__




