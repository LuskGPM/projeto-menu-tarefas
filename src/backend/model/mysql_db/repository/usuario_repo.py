from ..entities import Usuario
from .mysql_repo import MySQLRepository
from sqlalchemy import select, and_

class UsuarioRepository(MySQLRepository):
    
    async def select_by_nickname(self, nickname) -> Usuario | None:
        async with self as db:
            statement = select(Usuario).where(Usuario.nickname == nickname)
            result = await db.session_async.execute(statement)
            return await result.scalar_one_or_none()
        
    async def validar_login(self, nickname: str, senha_hash: str) -> Usuario | None:
        async with self as db:
            statement = select(Usuario).where(and_(Usuario.nickname == nickname, Usuario.senha_hash == senha_hash))
            result = await db.session_async.execute(statement)
            return await result.scalar_one_or_none()
        
    async def nickname_exists(self, nickname) -> bool:
        async with self as db:
            statement = select(Usuario).where(Usuario.nickname == nickname)
            result = await db.session_async.execute(statement)
            return await result.scalar_one_or_none() is not None
