from datetime import date
from sqlalchemy.orm import Session
from domain.entities.Centro import Centro
from typing import Callable
from domain.repositories import CentroRepositoryBaseModel
from typing import NoReturn

class CentroRepository:

    database: Callable[[], Session]
    def __init__(self, session: Callable[[], Session]):
        self.database = session


    def save(self, centroSent: Centro) -> Centro:
        session = self.database()
        # TODO : verificar se o URM possui isso built in
        session.add(centroSent)
        session.commit()
        session.expunge_all()
        session.close()
        return centroSent

    def update(self, centroSent: Centro) -> NoReturn:
        session = self.database()
        session.merge(centroSent)
        session.commit()
        session.expunge_all()
        session.close()

    def find_all(self) -> list[Centro]:
        '''Função para fazer uma query de todas as SocialWorker da DB'''
        session = self.database()
        try:
            res = session.query(Centro).all()
            return res
        except Exception as e:
        # Lida com possíveis erros durante a consulta
            print(f"Erro durante a busca por data: {e}")
            return None
        finally:
            session.close()

    

    def delete_by_id(self, centro_id: int) -> NoReturn:
        """Função para deletar um Centro do DB, caso exista"""
        session = self.database()
        Centro_session = session.query(Centro).filter(Centro.id == centro_id).first()

        if Centro_session is not None:
            session.delete(Centro_session)
            session.commit()

        session.close()

    def find_by_id(self, centro_id: int) -> Centro | None:
        """Faz uma busca pelo id no banco e retorna o objeto"""
        session = self.database()
        session.close()
        return session.query(Centro).filter(Centro.id == centro_id).first()
    
    def find_by_data(self, data: str) -> list[Centro] | None:
        """Faz uma busca pelo id no banco e retorna o objeto"""
        session = self.database()
        try:
            centros = session.query(Centro).filter(Centro.data_agendada == data).all()
            return centros
        except Exception as e:
        # Lida com possíveis erros durante a consulta
            print(f"Erro durante a busca por data: {e}")
            return None
        finally:
            session.close()
    


assert isinstance(CentroRepository(
    {}), CentroRepositoryBaseModel.CentroRepositoryBaseModel)