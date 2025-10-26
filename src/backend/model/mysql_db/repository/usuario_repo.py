from ..entities import Usuario
from .mysql_repo import MySQLRepository

class UsuarioRepository(MySQLRepository):
    
    def select_by_nickname(self, nickname) -> Usuario | None:
        with self as db:
            return db.session.query(Usuario).filter_by(nickname = nickname)
        
    def validar_login(self, nickname: str, senha: str) -> Usuario | None:
        with self as db:
            return db.session.query(Usuario).filter_by(nickname = nickname, senha = senha).first()
        
    def nickname_exists(self, nickname) -> bool:
        with self as db:
            return db.session.query(Usuario).filter_by(nickname = nickname).first() is not None
        
