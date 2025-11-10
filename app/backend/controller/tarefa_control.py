from ..model.mysql_db import Tarefa, TarefaRepository
from ..api.schemas import TarefaCreate, TarefaUpdate
from .configs import RedisControl as RedCache, COMMON_KEYS, criar_key
from typing import Sequence
from .categoria_control import CategoriaControler
import asyncio

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
        cache_key = criar_key(COMMON_KEYS['TASK'], f'{tarefa.status}_{usuario_id}')
        cache = RedCache(cache_key)
        # 3 Excluí cache antigo
        await cache.excluir_cache()
    
    async def processar_tarefa_update(self, tarefa: TarefaUpdate, usuario_id: int) -> None:
        # 1. Busca tarefa existente
        tarefa_existente = await self._select_by_id(Tarefa, tarefa.usuario_id)
        if not tarefa_existente or tarefa_existente.usuario_id != usuario_id:
            raise ValueError('Tarefa não encontrada ou não pertence ao usuário')
        
        # 2. Atualiza campos fornecidos
        update_data = tarefa.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(tarefa_existente, key, value)
        
        # 3. Salva no banco
        await self._update(tarefa_existente)
        
        # 4. Limpa cache
        cache_key = criar_key(COMMON_KEYS['TASK'], f'{tarefa_existente.status}_{usuario_id}')
        cache = RedCache(cache_key)
        await cache.excluir_cache()
        
    async def processar_tarefa_delete(self, tarefa_id, usuario_id):
        await self._delete_tarefa(
            usuario_id = usuario_id,
            tarefa_id = tarefa_id
        )
        cache = RedCache(COMMON_KEYS['TASK'])
        await cache.excluir_cache()
        
    async def receber_tarefa_por_status(self, status: str, usuario_id: int) -> dict | list[dict]:
        # 1. Tenta buscar no cache primeiro
        cache_key = criar_key(COMMON_KEYS['TASK'], f'{status}_{usuario_id}')
        cache = RedCache(cache_key)
        cached_data = await cache.receber_cache()
        
        if cached_data:
            return cached_data
        
        # 2. Se não tem no cache, busca no MySQL
        tarefas: Sequence[Tarefa] = await self._select_by_status(status, usuario_id)
        categoria_control = CategoriaControler()
        tarefas_dict_list = []
        for tarefa in tarefas:
            # Obtém a categoria
            categoria = await categoria_control.obter_categoria_por_id(tarefa.categoria_id)
            # Dicionário da tarefa específica
            tarefa_dict = tarefa.to_dict()
            tarefa_dict['categoria_nome'] = categoria['nome']
            tarefa_dict['categoria_cor'] = categoria['cor']
            # Adiciona o dicionário na lista de tarefas
            tarefas_dict_list.append(tarefa_dict)
        # 3. Salva no cache para próximas consultas
        cache.adicionar_dados(tarefas_dict_list)
        await cache.processar_cache()
            
        return tarefas_dict_list
    
    async def receber_tarefas(self, usuario_id: int) -> dict | list[dict]:
        # Executa as 3 consultas simultaneamente
        pendentes = await self.receber_tarefa_por_status('pendente', usuario_id)
        em_andamento = await self.receber_tarefa_por_status('em_andamento', usuario_id)
        concluidas = await self.receber_tarefa_por_status('concluida', usuario_id)
        
        return pendentes + em_andamento + concluidas
