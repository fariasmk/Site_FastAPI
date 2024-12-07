from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from core.configs import settings
from models.tag_model import TagModel

# Tabela de associação entre autores e tags
tags_autor = Table(
    'tags_autor',
    settings.DBBaseModel.metadata,
    Column('id_autor', Integer, ForeignKey('autores.id')),
    Column('id_tag', Integer, ForeignKey('tags.id'))
)


class AutorModel(settings.DBBaseModel):
    """Autor das postagens no blog"""
    __tablename__: str = 'autores'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100))
    imagem: Mapped[str] = mapped_column(String(100))  # 40x40

    # Um autor pode ter várias tags
    tags: Mapped[List[TagModel]] = relationship(
        'TagModel',
        secondary=tags_autor,
        backref='taga',
        lazy='joined'
    )

    @property
    def get_tags_list(self) -> List[int]:
        return [int(tag.id) for tag in self.tags]

