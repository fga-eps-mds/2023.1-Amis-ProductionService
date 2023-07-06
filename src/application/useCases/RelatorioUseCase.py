from domain.entities.Relatorio import Relatorio
from domain.repositories.RelatorioRepositoryBaseModel import RelatorioRepositoryBaseModel
from typing import NoReturn

class RelatorioUseCase():
    __relatorioRepository__: RelatorioRepositoryBaseModel

    def __init__(
        self,
        relatorioRepository: RelatorioRepositoryBaseModel
    ):
        self.__relatorioRepository__ = relatorioRepository

    def save(self, relatorioSent: Relatorio) -> Relatorio:

        return self.__relatorioRepository__.save(relatorioSent=relatorioSent)

