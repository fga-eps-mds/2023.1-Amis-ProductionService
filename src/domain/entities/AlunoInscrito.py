'''Importando parâmetros da orm'''
from pydantic import BaseModel

class AlunoInscritoBase(BaseModel):
    nome: str
    login: str
    confirmado: bool
    centroId: int

class AlunoInscrito(AlunoInscritoBase):
    ...

class AlunoInscritoRequest(AlunoInscritoBase):
    ...

class AlunoInscritoRequestId(AlunoInscritoBase):
    ...

class AlunoInscritoResponse(AlunoInscritoBase):
    ...
