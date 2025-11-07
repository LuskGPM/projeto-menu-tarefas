from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from ...controller import UsuarioControler
from ..schemas import UsuarioCreate, UsuarioLogin, UsuarioUpdate
from ..dependencies import verificar_login

rotas_user = APIRouter()

@rotas_user.post('/api/user/register')
async def rota_user_cadastro(user_dados: UsuarioCreate) -> dict:
    try:
        user_control = UsuarioControler()
        verificar_nickname = await user_control.verificar_disponibilidade_nickname(user_dados.nickname)
        if verificar_nickname:
            return{'message': 'Usuario já cadastrado'}
        await user_control.processar_cadastro(user_dados)
        return {'message': 'Usuário cadastrado com sucesso'}
    except Exception as e:
        raise HTTPException(400, f'Erro ao cadastrar dados: {e}')
    
@rotas_user.post('/api/user/login')
async def rota_user_login(user_dados: UsuarioLogin) -> dict:
    try:
        user_control = UsuarioControler()
        await user_control.processar_login(user_dados)
        return {'message': 'sessão iniciada'}
    except Exception as e:
        raise HTTPException(400, f'Dados inválidos: {e}')
    
@rotas_user.get('/api/user/logout')
async def rota_user_logout() -> dict:
    try:
        user_control = UsuarioControler()
        await user_control.encerrar_sessao()
        return {'message': 'Sessão encerrada com sucesso'}
    except Exception as e:
        raise HTTPException(400, f'Sessão já está encerrada: {e}')

@rotas_user.put('/api/user/update', dependencies=[Depends(verificar_login)])
async def rota_user_update(user_data: UsuarioUpdate) -> dict:
    try:
        user_control = UsuarioControler()
        await user_control.processar_update(user_data)
        await user_control.esta_logado()
        return {'message': 'Dados atualizados com sucesso'}
    except Exception as e:
        raise HTTPException(400, f'Erro ao atualizar dados: {e}')
    
@rotas_user.get('/api/user/me', dependencies=[Depends(verificar_login)])
async def rota_user_me() -> JSONResponse:
    user_control = UsuarioControler()
    dados_sessao = await user_control.obter_dados_sessao()
    if dados_sessao:
        await user_control.esta_logado()
        return JSONResponse(dados_sessao, 200)
    raise HTTPException(500, 'Erro ao fornecer dados do usuario')

@rotas_user.get('/api/user/verificar-sessao', dependencies=[Depends(verificar_login)])
async def rota_user_verificar_sessao() -> JSONResponse:
    return JSONResponse(
        {
            'message': 'logado'
        }, 200
    )
    
@rotas_user.delete('/api/user/delete', dependencies=[Depends(verificar_login)])
async def rota_user_delete():
    try:
        user_control = UsuarioControler()
        dados_sessao = await user_control.obter_dados_sessao()
        await user_control.processar_delete(dados_sessao['id'])
        return {'message': 'Usuário deletado com sucesso'}
    except Exception as e:
        raise HTTPException(400, f'Erro ao deletar usuário: {e}')

@rotas_user.get('/')
async def hello_world() -> JSONResponse:
    return JSONResponse(
        {
            'Hello': 'World'
        },
        200
    )