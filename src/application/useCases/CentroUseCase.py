from domain.entities.Centro import Centro, CentroResponse, CentroBase, CentroRequestCodigo, Status, Turno
from domain.repositories.CentroRepositoryBaseModel import CentroRepositoryBaseModel
from infrastructure.repositories.fieldRepository import FieldValidation
from typing import NoReturn

class CentroUseCase():
    __centroRepository__: CentroRepositoryBaseModel

    def __init__(
        self,
        centroRepository: CentroRepositoryBaseModel
    ):
        self.__centroRepository__ = centroRepository

    def save(self, centroSent: Centro) -> Centro:
        '''Função para salvar um objeto Centro na DB, utilizada também como update'''
        return self.__centroRepository__.save(centroSent=centroSent)

    def delete_by_codigo(self, codigo: int) -> None:
        return self.__centroRepository__.delete_by_codigo(centro_codigo=codigo)

    def find_all(self) -> list[CentroResponse]:
        centros_db = self.__centroRepository__.find_all()
        centros = list()
        for centro_db in centros_db:
            centro = CentroResponse(
                descricao=centro_db.descricao,
                data_agendada=centro_db.data_agendada,
                status=centro_db.status,
                turno=centro_db.turno,
                codigo=centro_db.codigo
            )
            centros.append(centro)
        
        return centros
    

    def find_by_codigo(self, centro_codigo : int) -> CentroBase | None:
        return self.__centroRepository__.find_by_codigo(centro_codigo=centro_codigo)

    def update(self, centroSent: CentroRequestCodigo) -> NoReturn:
        """Sobrescreve os dados de um Centro, assume que ele já exista"""
        self.__centroRepository__.update(Centro(**centroSent.__dict__))


    def validate(self, centro: Centro) -> dict:
        fieldInfoDict = {}
        fieldInfoDict["descricao"] = vars(FieldValidation.descricaoValidation(
            centro.descricao))
        fieldInfoDict["data_agendada"] = vars(FieldValidation.dataValidation(centro.data_agendada))

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

        
