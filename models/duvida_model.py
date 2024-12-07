from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey
from core.configs import settings
from models.area_model import AreaModel


class DuvidaModel(settings.DBBaseModel):
    __tablename__ = 'duvidas'  # Nome pluralizado para consistência

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    id_area: Mapped[int] = mapped_column(
        Integer,
        ForeignKey('areas.id', ondelete='CASCADE'),
        nullable=False
    )
    area: Mapped['AreaModel'] = relationship('AreaModel', backref='duvidas', lazy='joined')

    titulo: Mapped[str] = mapped_column(String(200), nullable=False, index=True)
    resposta: Mapped[str] = mapped_column(String(400), nullable=False)

