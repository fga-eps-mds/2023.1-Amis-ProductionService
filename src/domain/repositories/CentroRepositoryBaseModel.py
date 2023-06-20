from datetime import date
from domain.entities.Centro import Centro
from sqlalchemy.orm import Session
from typing import Protocol, runtime_checkable, NoReturn



@runtime_checkable
class CentroRepositoryBaseModel(Protocol):

    def save(self, centroSent: Centro) -> Centro:
        '''Função para salvar um objeto assistente na DB'''
        ...

    def update(self, centroSent: Centro) -> NoReturn:
        """Funçãop para atualizar um Centro, assume que o Centro já existe."""
        ...

    def delete_by_id(self, centro_id: int)-> NoReturn:
        '''Função para apagar um Centro do banco pelo id'''
        ...

    def find_all(self, database: Session) -> list[Centro]:
        '''Função para fazer uma query de todas as SocialWorker da DB'''
        ...
    
    def find_by_id(self, centro_id: int) -> Centro | None:
        """Faz uma busca pelo id e retorna os dados do Centro caso existe"""
        ...

    def find_by_data(self, data: str) -> list[Centro] | None:

        ...