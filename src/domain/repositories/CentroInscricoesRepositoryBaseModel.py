from domain.entities.CentroInscricoes import CentroInscricoes
from domain.entities.AlunoInscrito import AlunoInscrito
from typing import Protocol, runtime_checkable


@runtime_checkable
class CentroInscricoesRepositoryBaseModel(Protocol):
    def save(self, CentroInscricoesSent: CentroInscricoes) -> CentroInscricoes:
        '''Função para salvar um objeto CentroInscricoes na DB'''
        ...
    
    def count_by_centro_id(self, centro_id: int) -> int:
        """Faz uma busca pelo id e retorna a quantidade de CentroInscricoes"""
        ...
    
    def list_inscricoes(self, centro_id: int) -> list[AlunoInscrito]:
        ...

    def confirmar_inscricao(self, centro_id: int, id_aluno: str) -> None:
        ...

    def deletar_inscricao(self, centro_id: int, id_aluno: str) -> None:
        ...
