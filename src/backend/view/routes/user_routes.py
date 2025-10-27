from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from ...controller import UsuarioControler

router_user = APIRouter()
user_controll = UsuarioControler()