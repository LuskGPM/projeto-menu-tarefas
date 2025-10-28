from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse
from ...controller import UsuarioControler
from ..schemas import UsuarioCreate, UsuarioLogin, UsuarioUpdate

rotas_user = APIRouter()

@rotas_user.post('/user/register')
async def rota_user_cadastro(user_dados: UsuarioCreate) -> dict:
    try:
        user_control = UsuarioControler()
        await user_control.processar_cadastro(user_dados)
        return {'message': 'Usuário cadastrado com sucesso'}
    except Exception as e:
        raise HTTPException(400, f'Erro ao cadastrar dados: {e}')
    
@rotas_user.post('/user/login')
async def rota_user_login(user_dados: UsuarioLogin):
    try:
        user_control = UsuarioControler()
        await user_control.processar_login(user_dados)
        return {'message': 'sessão iniciada'}
    except Exception as e:
        raise HTTPException(401, f'Dados inválidos')
    
@rotas_user.post('/user/logout')
async def rota_user_logout():
    try:
        user_control = UsuarioControler()
        await user_control.encerrar_sessao()
        return {'message': 'Sessão encerrada com sucesso'}
    except Exception as e:
        raise HTTPException(400, f'Sessão já está encerrada: {e}')

@rotas_user.put('/user/update')
async def rota_user_update(user_data: UsuarioUpdate):
    try:
        user_control = UsuarioControler()
        await user_control.processar_update(user_data)
        return {'message': 'Dados atualizados com sucesso'}
    except Exception as e:
        raise HTTPException(400, f'Erro ao atualizar dados: {e}')
    
@rotas_user.get('/user/me')
async def rota_user_me():
    user_control = UsuarioControler()
    dados_sessao = await user_control.obter_dados_sessao()
    if dados_sessao:
        return JSONResponse(dados_sessao, 200)
    raise HTTPException(500, 'Erro ao fornecer dados do usuario')
