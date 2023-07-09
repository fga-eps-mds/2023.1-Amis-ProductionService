from unittest import mock
from unittest.mock import MagicMock, patch
import pytest
from domain.entities.Centro import Centro, CentroRequest, CentroResponse, Status, Turno
from fastapi import HTTPException, status
from infrastructure.repositories.CentroRepository import CentroRepository
from sqlalchemy.orm import Session
import sys
from pathlib import Path

# Adiciona o diretório "src" ao caminho de importação
sys.path.append(str(Path(__file__).resolve().parents[3]))


def generate_session():
    return MagicMock(spec=Session)


    # Arrange
"""  
def test_find_all():
    database = generate_session()
    centroRepository = CentroRepository(database)
    expected_result = [Centro(), Centro()]
    database.query().all.return_value = expected_result

    # Act
    result = centroRepository.find_all()

    # Assert
    assert result == expected_result

 """
def test_save_new_centro():
    # Arrange
    database = generate_session()
    test_session = database

    centro = Centro(
        descricao='Criação de pastel',
        data_agendada='2000-01-01',
        status=1,
        turno=2,
        id=1
    )
    test_session.query().filter().first.return_value = None
    centroRepository = CentroRepository(database)

    # Act
    result = centroRepository.save(centro)

    # Assert
    assert result == centro

    test_session.close()

def test_invalidateCentro():
    # Arrange
    centro = Centro(
        descricao='Criação de pastel',
        data_agendada='-01',
        status=1,
        turno=2,
        id=1
    )

    database = generate_session()
    result = CentroRepository(database).validate_centro(centro)

    assert result['data_agendada']['status'] is False
    assert result['descricao']['status'] is True
    assert result['completeStatus'] is False


def test_validateCentro():
    # Arrange
    centro = Centro(
        descricao='Criação de pastel',
        data_agendada='2000-01-01',
        status=1,
        turno=2,
        id=1
    )
    database = generate_session()
    result = CentroRepository(database).validate_centro(centro)

    assert result['data_agendada']['status'] is True
    assert result['descricao']['status'] is True
    assert result['completeStatus'] is True
""" 

@mock.patch("infrastructure.repositories.CentroRepository.CentroRepository")
def test_find_all(mock_repository):
    # Criação do mock do repositório
    mock_repository_instance = mock_repository.return_value
    mock_repository_instance.find_all.return_value = [
        CentroResponse(
            descricao='Criação de pastel',
            data_agendada='2000-01-01',
            status=1,
            turno=2,
            id=1
        )
    ]
    centroRepository = mock_repository_instance
    centro = centroRepository.find_all()

    mock_repository_instance.find_all.assert_called_once()

    # Verifica o resultado retornado pela função
    assert len(centro) == 1
    assert centro[0].descricao == "Criação de pastel"
    assert centro[0].data_agendada == "2000-01-01"
    assert centro[0].status == Status.DISPONIVEL
    assert centro[0].turno == Turno.VESPERTINO
    assert centro[0].id == 1 

 """