import uvicorn
from fastapi import FastAPI
from ..routes import rotas_user

server = FastAPI()
server.include_router(rotas_user)
