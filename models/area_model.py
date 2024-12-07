from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String
from core.configs import settings

class AreaModel(settings.DBBaseModel):
    """Dúvidas respondidas no FAQ são categorizadas em áreas"""
    __tablename__ = 'areas'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    area: Mapped[str] = mapped_column(String(100), nullable=False)


