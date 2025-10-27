from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from ...controller import UsuarioControler

class UserRouter:
    def __init__(self):
        self.__user_route = APIRouter()
