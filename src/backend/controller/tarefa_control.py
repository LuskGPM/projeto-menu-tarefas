from ..model.mysql_db import Tarefa, TarefaRepository
from ..view.schemas import TarefaCreate
from .configs import RedisControl as RedCache, COMMON_KEYS
from .configs.cache import build_cache_key, ENTITIES, TAREFA_STATUS
from typing import Dict

class TarefaControler:
    def __init__(self):
        self.__repo_tarefa = TarefaRepository()
        
    def processar_tarefa(self, tarefa: TarefaCreate):
        # 1. Criar e inserir no MySQL
        new_tarefa = Tarefa(
            titulo = tarefa.titulo,
            descricao = tarefa.descricao,
            status = tarefa.status,
            prioridade = tarefa.prioridade,
            categoria_id = tarefa.categoria_id
        )
        self.__repo_tarefa.insert(new_tarefa)
        
        # 2. Cache no Redis (dados básicos da tarefa)
        tarefa_dict = {
            'titulo': tarefa.titulo,
            'descricao': tarefa.descricao,
            'status': tarefa.status,
            'prioridade': tarefa.prioridade,
            'categoria_id': tarefa.categoria_id
        }
        cache = RedCache(COMMON_KEYS['TAREFAS_PENDENTES'], tarefa_dict)
        cache.processar_hash_cache()
        
        # 3. Invalidar caches de listagem
        #self.__invalidate_status_cache(dados.get('status'))
        return tarefa_dict

    
    def __invalidate_status_cache(self, status: str):
        """Remove cache de listagem por status"""
        # Implementar limpeza de cache quando necessário
        pass
    
    def receber_tarefa_por_status(self, status: str = 'PENDENTE'):
        # 1. Tenta buscar no cache primeiro
        cache_key = build_cache_key(ENTITIES['TAREFA'], TAREFA_STATUS[status])
        cache = RedCache(cache_key)
        cached_data = cache.receber_hash_cache()
        
        if cached_data:
            return cached_data
        
        # 2. Se não tem no cache, busca no MySQL
        tarefas = self.__repo_tarefa.select_by_status(TAREFA_STATUS[status])
        tarefas_dict = [tarefa.to_dict() for tarefa in tarefas]
        
        # 3. Salva no cache para próximas consultas
        cache_with_data = RedCache(cache_key, {'tarefas': tarefas_dict})
        cache_with_data.processar_hash_cache()
            
        return tarefas_dict
