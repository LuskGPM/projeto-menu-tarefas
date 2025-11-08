from pydantic import BaseModel, Field
from typing import Literal

class TarefaCreate(BaseModel):
    titulo: str = Field(min_length=3, max_length=60)
    descricao: str
    status: Literal['pendente', 'em_andamento', 'concluida']
    prioridade: Literal['baixa', 'media', 'alta']
    categoria_id: int
    
class TarefaUpdate(BaseModel):
    titulo: str | None = Field(None, min_length=3, max_length=60)
    descricao: str| None = None
    status: Literal['pendente', 'em_andamento', 'concluida'] | None = None
    
class TarefaDelete(BaseModel):
    titulo: str | None = Field(None, min_length=3, max_length=60)
    status: Literal['pendente', 'em_andamento', 'concluida']
    prioridade: Literal['baixa', 'media', 'alta']
