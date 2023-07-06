from datetime import date
from sqlalchemy.orm import Session
from domain.entities.CentroInscricoes import CentroInscricoes
from domain.entities.AlunoInscrito import AlunoInscrito
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

    def list_inscricoes(self, centro_id: int) -> list[AlunoInscrito]:
        session = self.database()
        data = session.execute('''
            SELECT s.nome, s.login, c.confirmado, c.idCentro FROM centroProdInscricoes AS c 
            JOIN student AS s ON c.idAluno = s.login
            WHERE c.idCentro = :centro_id
        ''', {"centro_id": centro_id})

        formattedValues: list[AlunoInscrito] = [
            AlunoInscrito(nome=aluno[0], login=aluno[1], confirmado=bool(aluno[2]), centroId=aluno[3]) for aluno in data
        ]
        session.close()
        return formattedValues

    def confirmar_inscricao(self, centro_id: int, id_aluno: str):
        session = self.database()
        session.merge(CentroInscricoes(idCentro=centro_id, idAluno=id_aluno, confirmado=1))
        session.commit()
        session.expunge_all()
        session.close()
    
    def deletar_inscricao(self, centro_id: int, id_aluno: str):
        session = self.database()
        inscricao = session.query(CentroInscricoes).filter(
            CentroInscricoes.idCentro == centro_id
        ).filter(
            CentroInscricoes.idAluno == id_aluno
        ).first()

        if inscricao is not None:
            session.delete(inscricao)
            session.commit()

        session.close()

assert isinstance(CentroInscricoesRepository({}), CentroInscricoesRepositoryBaseModel.CentroInscricoesRepositoryBaseModel)
