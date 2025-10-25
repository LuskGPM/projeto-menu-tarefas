from ..connection import ConnectionMySQL
from ..entities import Usuario
from typing import List, Any

class MySQLRepository(ConnectionMySQL):
    
    def select(self, model: Any) -> List[Any]:
        with self as db:
            return db.session.query(model).all()
        
    def select_by_id(self, model: Any, id: int) -> Any | None:
        with self as db:
            return db.session.query(model).filter(model.id == id).first()
            
    def insert(self, obj: Any) -> None | Exception:
        with self as db:
            try:
                db.session.add(obj)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise Exception(f'<MySQLRepo>: Erro ao inserir: {str(e)}')
            
    def insert_multiples(self, list_obj: List[Any]) -> None | Exception:
        with self as db:
            try:
                for obj in list_obj:
                    db.session.add(obj)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise Exception(f'<MySQLRepo>: Erro ao inserir multiplos objetos: {str(e)}')
    
    def update(self, obj: Any) -> None | Exception:
        with self as db:
            try:
                db.session.merge(obj)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise Exception(f'<MySQLRepo>: Erro ao atualizar objeto: {str(e)}')

    def delete(self, model: Any, id: int) -> None | Exception:
        with self as db:
            try:
                db.session.query(model).filter(model.id == id).delete()
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise Exception(f'<MySQLRepo>: Erro ao deletar objeto: {str(e)}')
            