from datetime import date
from domain.entities.CentroInscricoes import CentroInscricoes
from sqlalchemy.orm import Session
from typing import Protocol, runtime_checkable, NoReturn


@runtime_checkable
class CentroInscricoesRepositoryBaseModel(Protocol):
    def save(self, CentroInscricoesSent: CentroInscricoes) -> CentroInscricoes:
        '''Função para salvar um objeto CentroInscricoes na DB'''
        ...
    
    def count_by_centro_id(self, centro_id: int) -> int:
        """Faz uma busca pelo id e retorna a quantidade de CentroInscricoes"""
        ...