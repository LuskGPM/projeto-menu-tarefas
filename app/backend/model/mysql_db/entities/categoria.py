from ..connection import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer

class Categoria(Base):
    __tablename__ = 'categoria'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(60), nullable=False)
    cor: Mapped[str] = mapped_column(String(7), nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'cor': self.cor
        }