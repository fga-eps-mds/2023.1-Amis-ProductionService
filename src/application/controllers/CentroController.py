from database import engine, Base
from fastapi import APIRouter, Response, status, status, HTTPException

from src.domain.entities.Centro import Centro, CentroRequest, CentroResponse, CentroRequestId
from src.domain.entities.CentroInscricoes import CentroInscricoes, CentroInscricoesResponse

from fastapi.encoders import jsonable_encoder

from application.controllers import centroUseCase
from application.controllers import centroInscricoesUseCase


Base.metadata.create_all(bind=engine)


router_centro = APIRouter(
    prefix="/centro",
    tags=["centro"]
)

@router_centro.get("/{id}/inscricoes")
def listInscricoes(id: int):
    return centroInscricoesUseCase.list_inscricoes(centro_id=id)

@router_centro.patch("/{idCentro}/inscricoes/{idAluno}")
def confirmarInscricao(idCentro: int, idAluno: str):
    return centroInscricoesUseCase.confirmar_inscricao(centro_id=idCentro, id_aluno=idAluno)

@router_centro.delete("/{idCentro}/inscricoes/{idAluno}")
def confirmarInscricao(idCentro: int, idAluno: str):
    return centroInscricoesUseCase.deletar_inscricao(centro_id=idCentro, id_aluno=idAluno)

@router_centro.post("/", status_code=status.HTTP_201_CREATED)
def create(centro_request: CentroRequest):
    centro = Centro(**centro_request.__dict__)
    fieldsValidation = centroUseCase.validate(centro)

    if not fieldsValidation['completeStatus']:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=fieldsValidation)
    
    if not centroUseCase.validate_status(centro.data_agendada, centro.turno):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="esse horário está ocupado")

    centroUseCase.save(centroSent=centro)

    return centro_request

@router_centro.post("/{idCentro}/inscrever/{idAluno}",
                    status_code=status.HTTP_201_CREATED,
                    response_model=CentroInscricoesResponse)
def subscribe(idCentro: int, idAluno: str):
    if centroUseCase.find_by_id(idCentro) is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail="centro não existente")

    centroInscricao = CentroInscricoes(idAluno=idAluno, idCentro=idCentro, confirmado=0)
    centroInscricoesUseCase.save(centroInscricao)

    return CentroInscricoesResponse(idAluno=idAluno, idCentro=idCentro, confirmado=0)

@router_centro.get("/", response_model=list[CentroResponse])
def find_all():
    centros = centroUseCase.find_all()
    serialized_centros = jsonable_encoder(centros)

    return serialized_centros

@router_centro.put("/{id}", status_code=status.HTTP_201_CREATED)
def update(id: int, centroSent: CentroRequestId):
    if centroUseCase.find_by_id(id) is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail="centro não existente")
    centroUseCase.update(centroSent)


@router_centro.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int):
    centro = centroUseCase.find_by_id(id)
    if centro is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="centro não encontrado")

    centroUseCase.delete_by_id(id=centro.id)

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router_centro.get("/{id}", response_model=CentroResponse)
def find_by_id(id: int):
    centro = centroUseCase.find_by_id(id)
    if centro is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="centro não encontrado")
    
    serialized_centro = jsonable_encoder(centro)

    return serialized_centro
