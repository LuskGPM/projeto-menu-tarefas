from ..model import Tarefa, TarefaRepository
from .cache import RedisControl as RedCache
from typing import Dict

class TarefaControler:
    def __init__(self):
        self.__repo_tarefa = TarefaRepository()
        
    def insert_tarefa(self, dados: Dict):
        try:
            # 1. Criar e inserir no MySQL
            new_tarefa = Tarefa(**dados)
            self.__repo_tarefa.insert(new_tarefa)
            
            # 2. Cache no Redis (dados da tarefa criada)
            tarefa_dict = new_tarefa.to_dict()
            RedCache(tarefa_dict, 'TAREFA').set_cache()
            
            # 3. Invalidar caches de listagem
            self.__invalidate_status_cache(dados.get('status'))
            
            return tarefa_dict
            
        except Exception as e:
            raise Exception(f'Erro ao inserir tarefa: {str(e)}')
    
    def __invalidate_status_cache(self, status: str):
        """Remove cache de listagem por status"""
        # Implementar limpeza de cache quando necessário
        pass
    
    def get_tarefa_by_status(self, status):
        cache_data = RedCache('TAREFA', status).get_cache()
        
        if cache_data:
            return cache_data
        
        tarefas = self.__repo_tarefa.select_by_status(status)
        tarefas_dict = [tarefa.to_dict() for tarefa in tarefas]
        
        for tarefa in tarefas_dict:
            RedCache(tarefa, 'TAREFA').set_cache()
            
        return tarefas_dict
