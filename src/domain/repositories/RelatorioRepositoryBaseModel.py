from datetime import date
from domain.entities.Relatorio import Relatorio
from sqlalchemy.orm import Session
from typing import Protocol, runtime_checkable, NoReturn



@runtime_checkable
class RelatorioRepositoryBaseModel(Protocol):

    def save(self, relatorioSent: Relatorio) -> Relatorio:
        '''Função para salvar um objeto assistente na DB'''
        ...