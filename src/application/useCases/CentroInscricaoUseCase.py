from src.domain.repositories.CentroInscricoesRepositoryBaseModel import CentroInscricoesRepositoryBaseModel
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

