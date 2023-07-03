'''Importando parâmetros da orm'''
from datetime import date
from enum import Enum
from sqlalchemy import Column, Integer, ForeignKey, String, Boolean
from database import Base
from pydantic import BaseModel

class CentroInscricoesBase(BaseModel):
    idCentro: int
    idAluno: str
    confirmado: bool

class CentroInscricoes(Base):
    '''Classe para estabelecer o modelo na tabela DB'''
    __tablename__ = "centroProdInscricoes"
    __table_args__ = {"extend_existing": True}
    idCentro: int = Column(Integer, ForeignKey("centroProd.id"), index=True, nullable = False, primary_key = True)
    idAluno: str = Column(String(length=255), nullable = False, primary_key = True)
    confirmado: bool = Column(Boolean, nullable=False, default=False)

class CentroInscricoesRequest(CentroInscricoesBase):
    '''...'''
    ...

class CentroInscricoesRequestId(CentroInscricoesBase):
    """Necessário para se fazer o update"""
    id : int

class CentroInscricoesResponse(CentroInscricoesBase):
    '''...'''
    # id: int
    class Config:
        orm_mode = True
