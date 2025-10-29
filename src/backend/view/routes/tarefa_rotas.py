from fastapi import APIRouter, Request, HTTPException, Depends
from fastapi.responses import JSONResponse
from ...controller import TarefaControler
from ..schemas import TarefaCreate, TarefaResponse, TarefaUpdate
from ..dependencies import verificar_login

rota_tarefa = APIRouter()

@rota_tarefa.post('/tarefa/register', dependencies=[Depends(verificar_login)])
async def rota_tarefa_cadastro(tarefa: TarefaCreate) -> dict | HTTPException:
    try:
        tarefa_control = TarefaControler()
        tarefa_control.processar_tarefa(tarefa)
        return {'message', 'Tarefa inserida com sucesso'}
    except Exception as e:
        raise HTTPException(f'Erro ao cadastrar tarefa: {e}')
    