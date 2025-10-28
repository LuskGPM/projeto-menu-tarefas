from ..model.mysql_db import Tarefa, TarefaRepository
from ..view.schemas import TarefaCreate
from .configs import RedisControl as RedCache, COMMON_KEYS
from .configs.cache import build_cache_key, ENTITIES, TAREFA_STATUS
from typing import Literal
import json

class TarefaControler(TarefaRepository):
    async def processar_tarefa(self, tarefa: TarefaCreate):
        # 1. Criar e inserir no MySQL
        new_tarefa = Tarefa(
            titulo = tarefa.titulo,
            descricao = tarefa.descricao,
            status = tarefa.status,
            prioridade = tarefa.prioridade,
            categoria_id = tarefa.categoria_id
        )
        await self._insert(new_tarefa)
        
        # 2. Cache no Redis (dados básicos da tarefa)
        tarefa_dict = {
            'titulo': tarefa.titulo,
            'descricao': tarefa.descricao,
            'status': tarefa.status,
            'prioridade': tarefa.prioridade,
            'categoria_id': tarefa.categoria_id
        }
        cache = RedCache(COMMON_KEYS['TAREFAS_PENDENTES'], tarefa_dict)
        await cache.processar_hash_cache()
        
        # 3. Invalidar caches de listagem
        #self.__invalidate_status_cache(dados.get('status'))
        return tarefa_dict

    
    def __invalidate_status_cache(self, status: str):
        """Remove cache de listagem por status"""
        # Implementar limpeza de cache quando necessário
        pass
    
    async def receber_tarefa_por_status(self, status: Literal['PENDENTE', 'EM_ANDAMENTO', 'CONCLUIDA']):
        # 1. Tenta buscar no cache primeiro
        cache_key = build_cache_key(ENTITIES['TAREFA'], TAREFA_STATUS[status])
        print(f'🔍 Buscando cache com chave: {cache_key}')
        cache = RedCache(cache_key)
        cached_data = await cache.receber_hash_cache()
        print(f'📦 Dados do cache: {cached_data}')
        
        if cached_data and 'tarefas' in cached_data:
            print('<TarefaControler>: Pegou do Redis')
            return json.loads(cached_data['tarefas'])
        print('<TarefaControler>: Pegou do Banco')
        
        # 2. Se não tem no cache, busca no MySQL
        tarefas = await self._select_by_status(TAREFA_STATUS[status])
        tarefas_dict = [tarefa.to_dict() for tarefa in tarefas]
        
        # 3. Salva no cache para próximas consultas
        print(f'💾 Salvando no cache com chave: {cache_key}')
        cache_with_data = RedCache(cache_key, {'tarefas': json.dumps(tarefas_dict)})
        await cache_with_data.processar_hash_cache()
        print('✅ Cache salvo!')
            
        return tarefas_dict
