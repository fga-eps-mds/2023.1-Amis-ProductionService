'''Importando parâmetros da orm'''
from datetime import date
from enum import Enum
from sqlalchemy import Column, Integer, String, Enum as EnumDB
from database import Base
from pydantic import BaseModel

class Status(Enum):
    DISPONIVEL=1
    INDISPONIVEL=2

class Turno(Enum):
    MATUTINO=1
    VESPERTINO=2
    NOTURNO=3
    DIURNO=4

class CentroBase(BaseModel):
    descricao: str
    data_agendada: str
    status: Status
    turno: Turno

class Centro(Base):
    '''Classe para estabelecer o modelo na tabela DB'''
    __tablename__ = "centroProd"
    __table_args__ = {"extend_existing": True}
    codigo: int = Column(Integer, primary_key = True)
    descricao : str = Column(String(170), nullable = False)
    data_agendada : str= Column(String(10), nullable = False)
    status: Enum = Column(EnumDB(Status), nullable = False)
    turno: Enum = Column(EnumDB(Turno), nullable=False)



class CentroRequest(CentroBase):
    '''...'''
    ...

class CentroRequestCodigo(CentroBase):
    """Necessário para se fazer o update"""
    codigo : int

class CentroResponse(CentroBase):
    '''...'''
    codigo: int
    class Config:
        orm_mode = True
