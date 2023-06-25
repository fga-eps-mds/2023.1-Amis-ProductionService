from database import get_db
from src.application.useCases.CentroUseCase import CentroUseCase
from src.infrastructure.repositories.CentroRepository import CentroRepository
from src.infrastructure.repositories.RelatorioRepository import RelatorioRepository
from src.application.useCases.RelatorioUseCase import RelatorioUseCase

from database import SessionLocal

databaseSessionGenerator = SessionLocal

centroRepository = CentroRepository(databaseSessionGenerator)

centroUseCase = CentroUseCase(centroRepository=centroRepository)

relatorioRepository = RelatorioRepository(databaseSessionGenerator)
relatorioUseCase= RelatorioUseCase(relatorioRepository=relatorioRepository)


