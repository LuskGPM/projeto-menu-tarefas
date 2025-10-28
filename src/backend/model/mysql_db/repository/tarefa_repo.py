from ..entities import Tarefa
from .mysql_repo import MySQLRepository
from sqlalchemy import select, Sequence

class TarefaRepository(MySQLRepository):
    
    async def _select_by_status(self, status: str) -> Sequence[Tarefa]:
        async with self as db:
            statement = select(Tarefa).where(Tarefa.status == status)
            result = await db.session_async.execute(statement)
            return result.scalars().all()
        
    async def _select_by_categoria(self, categoria_id: int) -> Sequence[Tarefa]:
        async with self as db:
            statement = select(Tarefa).where(Tarefa.categoria_id == categoria_id)
            result = await db.session_async.execute(statement)
            return result.scalars().all()
        
    async def _select_by_prioridade(self, prioridade: str) -> Sequence[Tarefa]:
        async with self as db:
            statement = select(Tarefa).where(Tarefa.prioridade == prioridade)
            result = await db.session_async.execute(statement)
            return result.scalars().all()
