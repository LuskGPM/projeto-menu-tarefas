from ..entities import Tarefa
from .mysql_repo import MySQLRepository
from sqlalchemy import select, delete, Sequence

class TarefaRepository(MySQLRepository):
    
    async def _select_by_prioridade(self, prioridade: str, usuario_id: int) -> Sequence[Tarefa]:
        async with self as db:
            statement = select(Tarefa).where(
                (Tarefa.prioridade == prioridade) &
                (Tarefa.usuario_id == usuario_id)
            )
            result = await db.session_async.execute(statement)
            return result.scalars().all()
        
    async def _select_by_id_user_tarefa(self, tarefa_id: int, usuario_id: int) -> Sequence[Tarefa]:
        async with self as db:
            statement = select(Tarefa).where(
                (Tarefa.id == tarefa_id) &
                (Tarefa.usuario_id == usuario_id)
            )
            result = await db.session_async.execute(statement)
            return result.scalar_one_or_none()
        
    async def _delete_tarefa(self, tarefa_id: int, usuario_id: int) -> None | Exception:
        async with self as db:
            try:
                statement = delete(Tarefa).where(
                    (Tarefa.usuario_id == usuario_id) &
                    (Tarefa.id == tarefa_id)
                )
                await db.session_async.execute(statement)
                await db.session_async.commit()
            except Exception as e:
                await db.session_async.rollback()
                raise Exception(f'Erro ao deletar tarefa: {e}')
            
