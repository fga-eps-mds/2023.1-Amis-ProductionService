from datetime import date
from sqlalchemy.orm import Session
from domain.entities.Relatorio import Relatorio
from typing import Callable
from domain.repositories import RelatorioRepositoryBaseModel
from typing import NoReturn

class RelatorioRepository:

    database: Callable[[], Session]
    def __init__(self, session: Callable[[], Session]):
        self.database = session


    def save(self, relatorioSent: Relatorio) -> Relatorio:
        session = self.database()
        # TODO : verificar se o URM possui isso built in
        session.add(relatorioSent)
        session.commit()
        session.expunge_all()
        session.close()
        return relatorioSent


assert isinstance(RelatorioRepository(
    {}), RelatorioRepositoryBaseModel.RelatorioRepositoryBaseModel)