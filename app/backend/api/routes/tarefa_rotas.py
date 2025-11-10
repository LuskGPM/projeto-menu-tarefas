from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from ...controller import TarefaControler, UsuarioControler
from ..schemas import TarefaCreate, TarefaUpdate, TarefaDelete
from ..dependencies import verificar_login

rotas_tarefas = APIRouter()

@rotas_tarefas.post('/api/tarefa/register', dependencies=[Depends(verificar_login)])
async def rota_tarefa_cadastro(tarefa: TarefaCreate) -> dict:
    try:
        tarefa_control = TarefaControler()
        user_control = UsuarioControler()
        
        dados_sessao = await user_control.obter_dados_sessao()
        usuario_id = dados_sessao['id']
        
        await tarefa_control.processar_tarefa_cadastro(tarefa, usuario_id)
        await user_control.esta_logado()
        
        return {'message': 'Tarefa inserida com sucesso'}
    except Exception as e:
        raise HTTPException(400, f'Erro ao cadastrar tarefa: {e}')
    
@rotas_tarefas.put('/api/tarefa/update', dependencies=[Depends(verificar_login)])
async def rota_tarefa_update(tarefa: TarefaUpdate) -> dict:
    try:
        user_control = UsuarioControler()
        tarefa_control = TarefaControler()
        
        dados_sessao = await user_control.obter_dados_sessao()
        usuario_id = dados_sessao['id']
        
        await tarefa_control.processar_tarefa_update(tarefa, usuario_id)
        await user_control.esta_logado()
        
        return {'message': 'Tarefa atualizada com sucesso'}
    except Exception as e:
        raise HTTPException(400, f'Erro ao atualizar tarefa: {e}')
    
@rotas_tarefas.get('/api/tarefa/all', dependencies=[Depends(verificar_login)])
async def rota_tarefa_get_all() -> JSONResponse:
    try:
        user_control = UsuarioControler()
        tarefa_control = TarefaControler()
        
        dados_sessao = await user_control.obter_dados_sessao()
        usuario_id = dados_sessao['id']

        tarefas = await tarefa_control.receber_tarefas(usuario_id)
        await user_control.esta_logado()
        
        return JSONResponse(tarefas, 200)
    except Exception as e:
        raise HTTPException(400, f'Erro ao solicitar todas as tarefas: {e}')

@rotas_tarefas.delete('/api/tarefa/delete', dependencies=[Depends(verificar_login)])
async def rota_tarefa_delete(tarefa: TarefaDelete):
    try:
        user_control = UsuarioControler()
        tarefa_control = TarefaControler()
        
        dados_sessao = await user_control.obter_dados_sessao()
        usuario_id = dados_sessao['id']
        
        await tarefa_control.processar_tarefa_delete(tarefa, usuario_id)
        await user_control.esta_logado()
        
        return {'message': 'Tarefa excluída com sucesso'}
    except Exception as e:
        raise HTTPException(400, f'Erro ao deletar tarefas: {e}')
