from dataclasses import dataclass
from datetime import datetime
from enum import Enum
import re


@dataclass
class fieldInfo:
    """Classe para armazenar informações sobre os campos de um modelo"""
    status: bool
    detail: str


class FieldValidation:
    """Validação quanto ao formato dos dados (não valida lógicas de negócio))"""
    @classmethod
    def nomeValidation(cls, nome: str) -> fieldInfo:
        if len(nome) > 70:
            return fieldInfo(False, "Nome muito grande")
        elif len(nome) == 0:
            return fieldInfo(False, "Nome não pode ser vazio")
        return fieldInfo(True, "Nome válido")

    @classmethod
    def dataValidation(cls, data_request: str) -> fieldInfo:
        data = str(data_request)
        pattern = r'^\d{4}-\d{2}-\d{2}$'
        if not re.match(pattern, data):
            return fieldInfo(False, "Formato data de agendamento inválida")

        try:
            datetime.strptime(data, '%Y-%m-%d')
        except Exception as e:
            return fieldInfo(False, f"Data de agendamento inválida ({e})")

        return fieldInfo(True, "Data de agendamento válida")

    @classmethod
    def descricaoValidation(cls, descricao:str):
        if len(descricao) > 170:
            return fieldInfo(False,"Descrição muito grande")
        return fieldInfo(True,"Descrição válida")
    
    @classmethod
    def vagasValidation(cls, vagas: int):
        if vagas <= 0:
            return fieldInfo(False, "Deve ter no minimo uma vaga")
    
        if vagas >= 2147483648: # 2^31
            return fieldInfo(False, "Vagas devem ser menores que 2147483648")

        return fieldInfo(True, "Vagas válida")
