from domain.entities.Centro import Centro, CentroResponse, CentroBase, CentroRequest
from domain.repositories.CentroRepositoryBaseModel import CentroRepositoryBaseModel
from domain.repositories.CentroInscricoesRepositoryBaseModel import CentroInscricoesRepositoryBaseModel
from infrastructure.repositories.fieldRepository import FieldValidation
from typing import NoReturn
class CentroUseCase():
    __centroRepository__: CentroRepositoryBaseModel
    __centroInscricoesRepository__: CentroInscricoesRepositoryBaseModel

    def __init__(
        self,
        centroRepository: CentroRepositoryBaseModel,
        centroInscricoesRepository: CentroInscricoesRepositoryBaseModel
    ):
        self.__centroRepository__ = centroRepository
        self.__centroInscricoesRepository__ = centroInscricoesRepository

    def save(self, centroSent: Centro) -> Centro:
        '''Função para salvar um objeto Centro na DB, utilizada também como update'''
        return self.__centroRepository__.save(centroSent=centroSent)

    def delete_by_id(self, id: int) -> None:
        return self.__centroRepository__.delete_by_id(centro_id=id)

    def find_all(self) -> list[CentroResponse]:
        centros_db = self.__centroRepository__.find_all()
        centros: list[CentroResponse] = list()
        for centro_db in centros_db:
            vagasOcupadas = self.__centroInscricoesRepository__.count_by_centro_id(centro_db.id)

            centro = CentroResponse(
                descricao=centro_db.descricao,
                data_agendada=centro_db.data_agendada,
                status=centro_db.status,
                turno=centro_db.turno,
                id=centro_db.id,
                vagas=centro_db.vagas,
                vagasRestantes = centro_db.vagas - vagasOcupadas
            )
            centros.append(centro)
        
        return centros
    

    def find_by_id(self, centro_id : int) -> CentroBase | None:
        return self.__centroRepository__.find_by_id(centro_id=centro_id)

    def update(self, centroSent: CentroRequest) -> NoReturn:
        """Sobrescreve os dados de um Centro, assume que ele já exista"""
        self.__centroRepository__.update(Centro(**centroSent.__dict__))


    def validate(self, centro: Centro) -> dict:
        fieldInfoDict = {}
        fieldInfoDict["descricao"] = vars(FieldValidation.descricaoValidation(
            centro.descricao))
        fieldInfoDict["data_agendada"] = vars(FieldValidation.dataValidation(centro.data_agendada))
        fieldInfoDict["vagas"] = vars(FieldValidation.vagasValidation(centro.vagas))

        completeStatus = True
        for key in fieldInfoDict:
            if fieldInfoDict[key]['status'] == False:
                completeStatus = False
                break
        fieldInfoDict['completeStatus'] = completeStatus

        return fieldInfoDict
    
    def validate_status(self, data, turno) -> bool:
        centros = self.__centroRepository__.find_by_data(data)
        if centros is not None:
            for centro in centros:
                if centro.turno.value == turno.value:
                    return False
        return True

        
