from core.configs import settings
from sqlalchemy import Integer, String
from sqlalchemy.orm import validates, Mapped, mapped_column, relationship
from typing import List

class TagModel(settings.DBBaseModel):
    __tablename__ = 'tags'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    tag: Mapped[str] = mapped_column(String(100), nullable=False, index=True)

    # Relacionamento com PostModel
    posts: Mapped[List['PostModel']] = relationship(
        'PostModel',
        secondary='tags_post',  # Nome da tabela associativa
        back_populates='tags',  # Nome da propriedade correspondente em PostModel
        lazy='select'
    )

    @validates('tag')
    def validate_tag(self, key, value: str) -> str:
        value = value.strip()  # Remove espaços extras
        if not value or len(value) < 2:
            raise ValueError("A tag deve conter pelo menos 2 caracteres.")
        return value

