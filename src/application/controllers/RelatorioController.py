from database import engine, Base
from fastapi import APIRouter, Response, status, status, HTTPException
from src.domain.entities.Relatorio import Relatorio, RelatorioRequest
from fastapi.encoders import jsonable_encoder

from application.controllers import relatorioUseCase

Base.metadata.create_all(bind=engine)


router_relatorio = APIRouter(
    prefix="/relatorio",
    tags=["relatorio"]
)

@router_relatorio.post("/", status_code=status.HTTP_201_CREATED)
def create(relatorio_request: RelatorioRequest):
    relatorio = Relatorio(**relatorio_request.__dict__)

    relatorioUseCase.save(relatorioSent=relatorio)

    return relatorio_request