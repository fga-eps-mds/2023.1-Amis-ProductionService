from database import get_db
from src.application.useCases.CentroUseCase import CentroUseCase
from src.infrastructure.repositories.CentroRepository import CentroRepository

from database import SessionLocal

databaseSessionGenerator = SessionLocal

centroRepository = CentroRepository(databaseSessionGenerator)

centroUseCase = CentroUseCase(centroRepository=centroRepository)



