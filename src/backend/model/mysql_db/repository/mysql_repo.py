from ..connection import ConnectionMySQL
from sqlalchemy import select, delete, Sequence
from typing import List, Any

class MySQLRepository(ConnectionMySQL):
    
    async def _select(self, model: Any) -> Sequence[Any]:
        async with self as db:
            statement = select(model)
            result = await db.session_async.execute(statement)
            return result.scalars().all()
        
    async def _select_by_id(self, model: Any, id: int) -> Any | None:
        async with self as db:
            statement = select(model).where(model.id == id)
            result = await db.session_async.execute(statement)
            return result.scalar_one_or_none()
            
    async def _insert(self, obj: Any) -> None | Exception:
        async with self as db:
            try:
                db.session_async.add(obj)
                await db.session_async.commit()
            except Exception as e:
                await db.session_async.rollback()
                raise Exception(f'<MySQLRepo>: Erro ao inserir: {str(e)}')
            
    async def _insert_multiples(self, list_obj: List[Any]) -> None | Exception:
        async with self as db:
            try:
                db.session_async.add_all(list_obj)
                await db.session_async.commit()
            except Exception as e:
                await db.session_async.rollback()
                raise Exception(f'<MySQLRepo>: Erro ao inserir multiplos objetos: {str(e)}')
    
    async def _update(self, obj: Any) -> None | Exception:
        async with self as db:
            try:
                await db.session_async.merge(obj)
                await db.session_async.commit()
            except Exception as e:
                await db.session_async.rollback()
                raise Exception(f'<MySQLRepo>: Erro ao atualizar objeto: {str(e)}')

    async def _delete(self, model: Any, id: int) -> None | Exception:
        async with self as db:
            try:
                statement = delete(model).where(model.id == id)
                await db.session_async.execute(statement)
                await db.session_async.commit()
            except Exception as e:
                await db.session_async.rollback()
                raise Exception(f'<MySQLRepo>: Erro ao deletar objeto: {str(e)}')
            