'''Importando parâmetros da orm'''
from datetime import date
from enum import Enum
from sqlalchemy import Column, Integer, String, Enum as EnumDB
from database import Base
from pydantic import BaseModel

class Status(Enum):
    PRESENTE=1
    AUSENTE=2

class RelatorioBase(BaseModel):
    comentario : str
    status: Status
    nota: int 
    quantidade_produzida : str
    quantidade_desejada : str

class Relatorio(Base):
    __tablename__ = "relatorio"
    id: int = Column(Integer, primary_key = True, index= True)
    nome_aluno : str = Column(String(170), nullable = False)
    comentario : str= Column(String(500), nullable = False)
    status: Enum = Column(EnumDB(Status), nullable = False)
    nota: int = Column(Integer, nullable=False)
    quantidade_produzida : str= Column(String(10), nullable = True)
    quantidade_desejada : str= Column(String(10), nullable = True)



class RelatorioRequest(RelatorioBase):
    '''...'''
    ...

class RelatorioRequestId(RelatorioBase):
    """Necessário para se fazer o update"""
    id : int

class RelatorioResponse(RelatorioBase):
    '''...'''
    id: int
    class Config:
        orm_mode = True
