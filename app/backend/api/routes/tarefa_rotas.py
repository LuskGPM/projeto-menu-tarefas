from fastapi import APIRouter, Request, HTTPException, Depends
from fastapi.responses import JSONResponse
from ...controller import TarefaControler
from ..schemas import TarefaCreate, TarefaResponse, TarefaUpdate
from ..dependencies import verificar_login

rotas_tarefas = APIRouter()

@rotas_tarefas.post('/api/tarefa/register', dependencies=[Depends(verificar_login)])
async def rota_tarefa_cadastro(tarefa: TarefaCreate) -> dict:
    try:
        tarefa_control = TarefaControler()
        await tarefa_control.processar_tarefa(tarefa)
        return {'message': 'Tarefa inserida com sucesso'}
    except Exception as e:
        raise HTTPException(400, f'Erro ao cadastrar tarefa: {e}')
    
@rotas_tarefas.get('/api/tarefa')
async def rota_tarefa_get_all(request: Request):
    try:
        tarefa_control = TarefaControler()
        tarefas = await tarefa_control.receber_tarefas()
        return JSONResponse(tarefas, 200)
    except Exception as e:
        raise HTTPException(400, f'Erro ao solicitar todas as tarefas: {e}')
