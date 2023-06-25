from dotenv import load_dotenv
load_dotenv()
#importa a rota aqui

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from application.controllers.CentroController import router_centro
from application.controllers.RelatorioController import router_relatorio
load_dotenv()
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router_centro)
app.include_router(router_relatorio)

@app.get('/')
async def root():
    return {"message": "Amis !"}