from application.useCases.RelatorioUseCase import RelatorioUseCase
from infrastructure.repositories.RelatorioRepository import RelatorioRepository
from domain.entities.Relatorio import Relatorio
from unittest.mock import MagicMock
import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock

test_session = UnifiedAlchemyMagicMock()


def get_mock_db_session():
    """Callable do db em mock para o repository"""
    return test_session


relatorio_rep = RelatorioRepository(session=get_mock_db_session)
relatorio_use_case = RelatorioUseCase(
    relatorioRepository=relatorio_rep,
)

test_list = [
    (Relatorio(
        nome_aluno="Bianca Brasil",
        comentario = "Muito bom!",
        status= "Presente",
        nota= 10 ,
        quantidade_produzida = 10,
        quantidade_desejada = 10,
    )),
    (Relatorio(
        nome_aluno="Pedro Henrique",
        comentario = "Muito bom!",
        status= "Presente",
        nota= 10 ,
        quantidade_produzida = 10,
        quantidade_desejada = 10,
    )),
]


@pytest.mark.parametrize(
    "relatorioSent",
    test_list,
)


def test_save_relatorio_valido(relatorioSent):
    """Testa se o relatorio é salvo com sucesso, assume que sempre recebe um curso válido"""
    response = relatorio_use_case.save(relatorioSent=relatorioSent)
    assert relatorioSent == response, response.__dict__