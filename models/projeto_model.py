from datetime import datetime
from core.configs import settings
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column


class ProjetoModel(settings.DBBaseModel):
    """No website temos um portfólio de projetos"""
    __tablename__ = 'projetos'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    data: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, index=True)

    titulo: Mapped[str] = mapped_column(String(100), nullable=False)
    descricao_inicial: Mapped[str] = mapped_column(String(300), nullable=False)

    # Considerando maior flexibilidade para nomes de arquivos ou URLs
    imagem1: Mapped[str] = mapped_column(String(255), nullable=True)
    imagem2: Mapped[str] = mapped_column(String(255), nullable=True)
    imagem3: Mapped[str] = mapped_column(String(255), nullable=True)

    descricao_final: Mapped[str] = mapped_column(String(300), nullable=True)

    # URLs podem ser longas, então aumentando o tamanho
    link: Mapped[str] = mapped_column(String(500), nullable=True)  # Tamanho maior para URLs
