from ..entities import Usuario
from .mysql_repo import MySQLRepository
from sqlalchemy import select, exists

class UsuarioRepository(MySQLRepository):
    
    async def _select_by_nickname(self, nickname) -> Usuario | None:
        async with self as db:
            statement = select(Usuario).where(Usuario.nickname == nickname)
            result = await db.session_async.execute(statement)
            return result.scalar_one_or_none()
        
    async def _nickname_exists(self, nickname) -> bool:
        async with self as db:
            statement = select(exists().where(Usuario.nickname == nickname))
            result = await db.session_async.execute(statement)
            return result.scalar()
        