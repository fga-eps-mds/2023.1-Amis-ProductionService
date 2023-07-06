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
    nome_aluno:str
    comentario : str
    status: str
    nota: int 
    quantidade_produzida : int
    quantidade_desejada : int

class Relatorio(Base):
    __tablename__ = "relatorio"
    __table_args__ = {"extend_existing": True}
    id: int = Column(Integer, primary_key = True, index= True)
    nome_aluno : str = Column(String(170), nullable = False)
    comentario : str= Column(String(500), nullable = False)
    status: str = Column(String(100), nullable = False)
    nota: int = Column(Integer, nullable=False)
    quantidade_produzida : int= Column(Integer, nullable = True)
    quantidade_desejada : int= Column(Integer, nullable = True)



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
