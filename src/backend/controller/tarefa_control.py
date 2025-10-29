from ..model.mysql_db import Tarefa, TarefaRepository
from ..api.schemas import TarefaCreate
from .configs import RedisControl as RedCache, COMMON_KEYS, criar_key
from typing import Literal, Sequence
import json

class TarefaControler(TarefaRepository):
    async def processar_tarefa(self, tarefa: TarefaCreate) -> None:
        # 1. Criar e inserir no MySQL
        new_tarefa = Tarefa(
            titulo = tarefa.titulo,
            descricao = tarefa.descricao,
            status = tarefa.status,
            prioridade = tarefa.prioridade,
            categoria_id = tarefa.categoria_id
        )
        await self._insert(new_tarefa)
    
        # 2. Cache no Redis
        cache_key = criar_key(COMMON_KEYS['TASK'], tarefa.status)
        cache = RedCache(cache_key)
        # 3 Excluí cache antigo
        await cache.excluir_cache()
    
    async def receber_tarefa_por_status(self, status: Literal['pendente', 'em_andamento', 'concluida']):
        # 1. Tenta buscar no cache primeiro
        cache_key = criar_key(COMMON_KEYS['TASK'], status)
        cache = RedCache(cache_key)
        cached_data = await cache.receber_cache()
        
        if cached_data:
            return cached_data
        
        # 2. Se não tem no cache, busca no MySQL
        tarefas: Sequence[Tarefa] = await self._select_by_status(status)
        tarefas_dict = [t.to_dict() for t in tarefas]
        
        # 3. Salva no cache para próximas consultas
        cache.adicionar_dados(tarefas_dict)
        await cache.processar_cache()
            
        return tarefas_dict
    
    async def receber_tarefas(self):
        pendentes = await self.receber_tarefa_por_status('pendente')
        em_andamento = await self.receber_tarefa_por_status('em_andamento')
        concluidas = await self.receber_tarefa_por_status('concluida')
        
        return pendentes + em_andamento + concluidas
    
