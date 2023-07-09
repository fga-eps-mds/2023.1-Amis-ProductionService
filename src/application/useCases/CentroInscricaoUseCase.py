from domain.repositories.CentroInscricoesRepositoryBaseModel import CentroInscricoesRepositoryBaseModel
from domain.entities.CentroInscricoes import CentroInscricoes
class CentroInscricoesUseCase():
    __centroInscricoesRepository__: CentroInscricoesRepositoryBaseModel

    def __init__(
        self,
        centroInscricoesRepository: CentroInscricoesRepositoryBaseModel
    ):
        self.__centroInscricoesRepository__ = centroInscricoesRepository

    def save(self, centroInscricoesSent: CentroInscricoes) -> CentroInscricoes:
        '''Função para salvar um objeto CentroInscricoes na DB, utilizada também como update'''
        return self.__centroInscricoesRepository__.save(centroInscricoesSent=centroInscricoesSent)

    def list_inscricoes(self, centro_id: int):
        return self.__centroInscricoesRepository__.list_inscricoes(centro_id=centro_id)
    
    def confirmar_inscricao(self, centro_id: int, id_aluno: str):
        return self.__centroInscricoesRepository__.confirmar_inscricao(centro_id=centro_id, id_aluno=id_aluno)

    def deletar_inscricao(self, centro_id: int, id_aluno: str) -> None:
        return self.__centroInscricoesRepository__.deletar_inscricao(centro_id=centro_id, id_aluno=id_aluno)