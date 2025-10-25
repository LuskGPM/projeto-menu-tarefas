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
    data_criacao: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    data_atualizacao: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())
    