from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates, Mapped, mapped_column
from core.configs import settings


class MembroModel(settings.DBBaseModel):
    __tablename__ = 'membros'  # Nome da tabela definido corretamente

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    funcao: Mapped[str] = mapped_column(String(100), nullable=False)
    imagem: Mapped[str] = mapped_column(String(255), nullable=False)  # Considerando um tamanho maior para a imagem

    @validates('funcao')
    def _valida_funcao(self, key, value):
        # Verifica se o valor não é vazio ou apenas espaços
        if not value.strip():
            raise ValueError("O campo 'função' é obrigatório e não pode ser vazio.")

        # Verifica se a função menciona 'Python'
        if 'Python' not in value:
            raise ValueError("A função deve mencionar 'Python'.")

        return value
