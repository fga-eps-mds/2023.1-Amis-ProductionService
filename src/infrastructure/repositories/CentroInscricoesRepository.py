from datetime import date
from sqlalchemy.orm import Session
from domain.entities.CentroInscricoes import CentroInscricoes
from typing import Callable
from domain.repositories import CentroInscricoesRepositoryBaseModel

class CentroInscricoesRepository:
    database: Callable[[], Session]
    def __init__(self, session: Callable[[], Session]):
        self.database = session


    def save(self, centroInscricoesSent: CentroInscricoes) -> CentroInscricoes:
        '''Função para salvar um objeto CentroInscricoes na DB'''
        session = self.database()
        # TODO : verificar se o URM possui isso built in
        session.add(centroInscricoesSent)
        session.commit()
        session.expunge_all()
        session.close()
        return centroInscricoesSent
    
    def count_by_centro_id(self, centro_id: int) -> int:
        """Faz uma busca pelo id e retorna a quantidade de CentroInscricoes"""
        session = self.database()
        quantity = session.query(CentroInscricoes).filter(CentroInscricoes.idCentro == centro_id).count()
        session.close()

        return quantity

assert isinstance(CentroInscricoesRepository({}), CentroInscricoesRepositoryBaseModel.CentroInscricoesRepositoryBaseModel)
