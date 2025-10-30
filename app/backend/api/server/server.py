import uvicorn
from fastapi import FastAPI
from ..routes import rotas_user, rotas_tarefas

server = FastAPI()
server.include_router(rotas_user)
server.include_router(rotas_tarefas)
