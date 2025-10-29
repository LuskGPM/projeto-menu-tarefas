from fastapi import APIRouter, Request, HTTPException, Depends
from fastapi.responses import JSONResponse
from ...controller import UsuarioControler
from ..schemas import UsuarioCreate, UsuarioLogin, UsuarioUpdate
from ..dependencies import verificar_login

rotas_user = APIRouter()

@rotas_user.post('/user/register')
async def rota_user_cadastro(user_dados: UsuarioCreate) -> dict | HTTPException:
    try:
        user_control = UsuarioControler()
        verificar_nickname = await user_control.verificar_disponibilidade_nickname(user_dados.nickname)
        if verificar_nickname:
            return{'message': 'Usuario já cadastrado'}
        await user_control.processar_cadastro(user_dados)
        return {'message': 'Usuário cadastrado com sucesso'}
    except Exception as e:
        raise HTTPException(400, f'Erro ao cadastrar dados: {e}')
    
@rotas_user.post('/user/login')
async def rota_user_login(user_dados: UsuarioLogin) -> dict | HTTPException:
    try:
        user_control = UsuarioControler()
        await user_control.processar_login(user_dados)
        return {'message': 'sessão iniciada'}
    except Exception as e:
        raise HTTPException(401, f'Dados inválidos')
    
@rotas_user.post('/user/logout', dependencies=[Depends(verificar_login)])
async def rota_user_logout() -> dict | HTTPException:
    try:
        user_control = UsuarioControler()
        await user_control.encerrar_sessao()
        return {'message': 'Sessão encerrada com sucesso'}
    except Exception as e:
        raise HTTPException(400, f'Sessão já está encerrada: {e}')

@rotas_user.put('/user/update', dependencies=[Depends(verificar_login)])
async def rota_user_update(user_data: UsuarioUpdate) -> dict | HTTPException:
    try:
        user_control = UsuarioControler()
        await user_control.processar_update(user_data)
        return {'message': 'Dados atualizados com sucesso'}
    except Exception as e:
        raise HTTPException(400, f'Erro ao atualizar dados: {e}')
    
@rotas_user.get('/user/me', dependencies=[Depends(verificar_login)])
async def rota_user_me(request: Request) -> JSONResponse | HTTPException:
    user_control = UsuarioControler()
    dados_sessao = await user_control.obter_dados_sessao()
    if dados_sessao:
        return JSONResponse(dados_sessao, 200)
    raise HTTPException(500, 'Erro ao fornecer dados do usuario')

@rotas_user.get('/')
async def hello_world(request: Request) -> JSONResponse:
    return JSONResponse(
        {
            'Hello': 'World'
        },
        200
    )