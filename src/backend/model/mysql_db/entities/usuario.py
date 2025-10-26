from ..connection import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer

class Usuario(Base):
    __tablename__ = 'usuario'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(60), nullable=False)
    nickname: Mapped[str] = mapped_column(String(90), nullable=False, unique=True)
    senha: Mapped[str] = mapped_column(String(255), nullable=False)
    
    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'nome': self.nome,
            'nickname': self.nickname
        }