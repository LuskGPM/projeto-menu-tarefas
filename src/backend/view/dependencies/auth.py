from ...controller import UsuarioControler
from fastapi import HTTPException

async def verificar_login():
    controller = UsuarioControler()
    if not await controller.esta_logado():
        raise HTTPException(401, 'Usuário não está logado')
    