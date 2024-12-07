#Postgres
# from pydantic_settings import BaseSettings
# from sqlalchemy.ext.declarative import declarative_base
# from fastapi.templating import Jinja2Templates
# from pydantic_settings import BaseSettings
# from sqlalchemy.ext.declarative import declarative_base
# from fastapi.templating import Jinja2Templates
# from pathlib import Path
# from typing import ClassVar
#
# class Settings(BaseSettings):
#     DB_URL: ClassVar[str] = 'postgresql+asyncpg://{Caminho do DB}'
#     DBBaseModel: ClassVar = declarative_base()
#     TEMPLATES: ClassVar[Jinja2Templates] = Jinja2Templates(directory='templates')
#     MEDIA: ClassVar[Path] = Path('media')
#
#     class Config:
#         case_sensitive = True
#
#
# settings = Settings()

#SQLITE
from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from fastapi.templating import Jinja2Templates
from pathlib import Path
from typing import ClassVar
import os


class Settings(BaseSettings):
    # Caminho do banco de dados SQLite
    DB_DIR: ClassVar[Path] = Path('db')  # Diretório do banco
    DB_FILE: ClassVar[Path] = DB_DIR / 'data.db'  # Nome do arquivo do banco
    DB_URL: ClassVar[str] = f'sqlite+aiosqlite:///{DB_FILE}'  # URL do banco SQLite

    # Modelo base do SQLAlchemy
    DBBaseModel: ClassVar = declarative_base()

    # Configuração de templates
    TEMPLATES: ClassVar[Jinja2Templates] = Jinja2Templates(directory='templates')

    # Diretório de arquivos de mídia
    MEDIA: ClassVar[Path] = Path('media')

    class Config:
        case_sensitive = True


# Verifica e cria a pasta do banco de dados, se necessário
os.makedirs(Settings.DB_DIR, exist_ok=True)

# Instância da configuração
settings = Settings()


