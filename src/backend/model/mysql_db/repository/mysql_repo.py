from ..connection import ConnectionMySQL
from sqlalchemy import select, delete
from typing import List, Any

class MySQLRepository(ConnectionMySQL):
    
    async def select(self, model: Any) -> List[Any]:
        async with self as db:
            result = await db.session_async.execute(select(model))
            return result.scalars().all()
        
    async def select_by_id(self, model: Any, id: int) -> Any | None:
        async with self as db:
            result = await db.session_async.execute(select(model).where(model.id == id))
            return await result.scalar_one_or_none()
            
    async def insert(self, obj: Any) -> None | Exception:
        async with self as db:
            try:
                db.session_async.add(obj)
                await db.session_async.commit()
            except Exception as e:
                await db.session_async.rollback()
                raise Exception(f'<MySQLRepo>: Erro ao inserir: {str(e)}')
            
    async def insert_multiples(self, list_obj: List[Any]) -> None | Exception:
        async with self as db:
            try:
                db.session_async.add_all(list_obj)
                await db.session_async.commit()
            except Exception as e:
                await db.session_async.rollback()
                raise Exception(f'<MySQLRepo>: Erro ao inserir multiplos objetos: {str(e)}')
    
    async def update(self, obj: Any) -> None | Exception:
        async with self as db:
            try:
                db.session_async.merge(obj)
                await db.session_async.commit()
            except Exception as e:
                await db.session_async.rollback()
                raise Exception(f'<MySQLRepo>: Erro ao atualizar objeto: {str(e)}')

    async def delete(self, model: Any, id: int) -> None | Exception:
        async with self as db:
            try:
                await db.session_async.execute(delete(model).where(model.id == id))
                await db.session_async.commit()
            except Exception as e:
                await db.session_async.rollback()
                raise Exception(f'<MySQLRepo>: Erro ao deletar objeto: {str(e)}')
            