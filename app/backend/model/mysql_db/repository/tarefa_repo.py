from ..entities import Tarefa
from .mysql_repo import MySQLRepository
from sqlalchemy import select, Sequence

class TarefaRepository(MySQLRepository):
    
    async def _select_by_status(self, status: str, usuario_id: int) -> Sequence[Tarefa]:
        async with self as db:
            statement = select(Tarefa).where(
                (Tarefa.status == status) &
                (Tarefa.usuario_id == usuario_id)
            )
            result = await db.session_async.execute(statement)
            return result.scalars().all()
        
    async def _select_by_categoria(self, categoria_id: int, usuario_id: int) -> Sequence[Tarefa]:
        async with self as db:
            statement = select(Tarefa).where(
                (Tarefa.categoria_id == categoria_id) &
                (Tarefa.usuario_id == usuario_id)
            )
            result = await db.session_async.execute(statement)
            return result.scalars().all()
        
    async def _select_by_prioridade(self, prioridade: str, usuario_id: int) -> Sequence[Tarefa]:
        async with self as db:
            statement = select(Tarefa).where(
                (Tarefa.prioridade == prioridade) &
                (Tarefa.usuario_id == usuario_id)
            )
            result = await db.session_async.execute(statement)
            return result.scalars().all()

    async def _select_all_by_user(self, usuario_id: int) -> Sequence[Tarefa]:
        async with self as db:
            statement = select(Tarefa).where(Tarefa.usuario_id == usuario_id)
            result = await db.session_async.execute(statement)
            return result.scalars().all()
        
    async def _delete_tarefa(self, titulo: str, status: str, prioridade: str, usuario_id: int) -> None | Exception:
        async with self as db:
            try:
                statement = select(Tarefa).where(
                    (Tarefa.usuario_id == usuario_id) &
                    (Tarefa.titulo == titulo) &
                    (Tarefa.status == status) &
                    (Tarefa.prioridade == prioridade)
                )
                await db.session_async.execute(statement)
                await db.session_async.commit()
            except Exception as e:
                await db.session_async.rollback()
                raise Exception(f'Erro ao deletar tarefa: {e}')
            
