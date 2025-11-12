from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ..routes import rotas_user, rotas_tarefas

server = FastAPI()
server.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # URL do seu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

server.include_router(rotas_user)
server.include_router(rotas_tarefas)
