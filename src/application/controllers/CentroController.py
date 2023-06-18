from database import engine, Base
from fastapi import APIRouter, Response, status, status, HTTPException
from src.domain.entities.Centro import Centro, CentroRequest, CentroRequestCodigo, CentroResponse
from fastapi.encoders import jsonable_encoder

from application.controllers import centroUseCase

Base.metadata.create_all(bind=engine)


router_centro = APIRouter(
    prefix="/centro",
    tags=["centro"]
)

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

@router_centro.get("/", response_model=list[CentroResponse])
def find_all():
    
    centros = centroUseCase.find_all()
    serialized_centros = jsonable_encoder(centros)

    return serialized_centros

@router_centro.put("/{codigo}", status_code=status.HTTP_201_CREATED)
def update(centroSent: CentroRequestCodigo):
    if centroUseCase.find_by_codigo(centroSent.codigo) is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail="centro não existente")
    centroUseCase.update(centroSent)


@router_centro.delete("/{codigo}", status_code=status.HTTP_204_NO_CONTENT)
def delete(codigo: int):
    centro = centroUseCase.find_by_codigo(codigo)
    if centro is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="centro não encontrado")

    centroUseCase.delete_by_codigo(codigo=centro.codigo)

    return Response(status_code=status.HTTP_204_NO_CONTENT)

