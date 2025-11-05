from ..connection import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, ForeignKey, DateTime, Enum, Text, func
from datetime import datetime

class Tarefa(Base):
    __tablename__ = 'tarefa'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    titulo: Mapped[str] = mapped_column(String(60), nullable=False)
    descricao: Mapped[str] = mapped_column(Text)
    status: Mapped[str] = mapped_column(Enum('pendente', 'em_andamento', 'concluida'), nullable=False)
    prioridade: Mapped[str] = mapped_column(Enum('baixa', 'media', 'alta'), nullable=False)
    categoria_id: Mapped[int] = mapped_column(Integer, ForeignKey('categoria.id'))
    usuario_id: Mapped[int] = mapped_column(Integer, ForeignKey('usuario.id'))
    data_criacao: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    data_atualizacao: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())
    
    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'titulo': self.titulo,
            'descricao': self.descricao,
            'status': self.status,
            'prioridade': self.prioridade,
            'categoria_id': self.categoria_id,
            'usuario_id': self.usuario_id,
            'data_criacao': self.data_criacao.isoformat() if self.data_criacao else None,
            'data_atualizacao': self.data_atualizacao.isoformat() if self.data_atualizacao else None
        }
    