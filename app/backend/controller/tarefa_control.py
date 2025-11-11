from ..model.mysql_db import Tarefa, TarefaRepository
from ..api.schemas import TarefaCreate, TarefaUpdate, TarefaDelete
from .configs import RedisControl as RedCache, COMMON_KEYS, criar_key
from typing import Sequence
from .categoria_control import CategoriaControler

class TarefaControler(TarefaRepository):
    async def processar_tarefa_cadastro(self, tarefa: TarefaCreate, usuario_id: int) -> None:
        # 1. Criar e inserir no MySQL
        new_tarefa = Tarefa(
            titulo = tarefa.titulo,
            descricao = tarefa.descricao,
            status = tarefa.status,
            prioridade = tarefa.prioridade,
            categoria_id = tarefa.categoria_id,
            usuario_id = usuario_id
        )
        await self._insert(new_tarefa)
        # 2. Cache no Redis
        cache_key = criar_key(COMMON_KEYS['TASK'], f'{tarefa.prioridade}_{usuario_id}')
        cache = RedCache(cache_key)
        # 3 Excluí cache antigo
        await cache.excluir_cache()
    
    async def processar_tarefa_update(self, tarefa: TarefaUpdate, usuario_id: int) -> None:
        # 1. Busca tarefa existente
        tarefa_existente = await self._select_by_id_user_tarefa(tarefa.id, usuario_id)
        if not tarefa_existente:
            raise ValueError('Tarefa não existe')
        
        # 2. Atualiza campos fornecidos
        update_data = tarefa.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(tarefa_existente, key, value)
        
        # 3. Salva no banco
        await self._update(tarefa_existente)
        
        # 4. Limpa cache
        cache_key = criar_key(COMMON_KEYS['TASK'], f'{tarefa_existente.prioridade}_{usuario_id}')
        cache = RedCache(cache_key)
        await cache.excluir_cache()
        
    async def processar_tarefa_delete(self, tarefa: TarefaDelete, usuario_id: int):
        await self._delete_tarefa(
            usuario_id = usuario_id,
            tarefa_id = tarefa.tarefa_id
        )
        cache_key = criar_key(COMMON_KEYS['TASK'], f'{tarefa.prioridade}_{usuario_id}')
        cache = RedCache(cache_key)
        await cache.excluir_cache()
        
    async def receber_tarefa_por_prioridade(self, prioridade: str, usuario_id: int) -> dict | list[dict]:
        # 1. Tenta buscar no cache primeiro
        cache_key = criar_key(COMMON_KEYS['TASK'], f'{prioridade}_{usuario_id}')
        cache = RedCache(cache_key)
        cached_data = await cache.receber_cache()
        
        if cached_data:
            return cached_data
        
        # 2. Se não tem no cache, busca no MySQL
        tarefas: Sequence[Tarefa] = await self._select_by_prioridade(prioridade, usuario_id)
        categoria_control = CategoriaControler()
        tarefas_dict_list = []
        for tarefa in tarefas:
            categoria = await categoria_control.obter_categoria_por_id(tarefa.categoria_id)
            # Dicionário da tarefa específica
            tarefa_dict = tarefa.to_dict()
            tarefa_dict['categoria_nome'] = categoria['nome']
            tarefa_dict['categoria_cor'] = categoria['cor']
            tarefas_dict_list.append(tarefa_dict)
        # 3. Salva no cache para próximas consultas
        cache.adicionar_dados(tarefas_dict_list)
        await cache.processar_cache()
            
        return tarefas_dict_list
    
    async def receber_tarefas(self, usuario_id: int) -> dict | list[dict]:
        alta = await self.receber_tarefa_por_prioridade('alta', usuario_id)
        media = await self.receber_tarefa_por_prioridade('media', usuario_id)
        baixa = await self.receber_tarefa_por_prioridade('baixa', usuario_id)
        
        return alta + media + baixa
