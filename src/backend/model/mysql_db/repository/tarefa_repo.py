from ..entities import Tarefa
from .mysql_repo import MySQLRepository
from typing import List

class TarefaRepository(MySQLRepository):
    
    def select_by_status(self, status: str) -> List[Tarefa] | None:
        with self as db:
            return db.session.query(Tarefa).filter_by(status = status).all()
        
    def select_by_categoria(self, categoria_id: int) -> List[Tarefa] | None:
        with self as db:
            return db.session.query(Tarefa).filter_by(categoria_id = categoria_id).all()
        
    def select_by_prioridade(self, prioridade: str) -> List[Tarefa] | None:
        with self as db:
            return db.session.query(Tarefa).filter_by(prioridade = prioridade).all()
        