from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from core.configs import settings
import models.__all_models  # Isso vai importar todos os modelos, incluindo AutorModel, PostModel, etc.

# Configuração do engine para SQLite
engine: AsyncEngine = create_async_engine(settings.DB_URL, echo=False)


# Função para criar a sessão assíncrona
def get_session() -> AsyncSession:
    __async_session = sessionmaker(
        autocommit=False,
        autoflush=False,
        expire_on_commit=False,
        class_=AsyncSession,
        bind=engine
    )
    session: AsyncSession = __async_session()
    return session


# Função para criar as tabelas na ordem correta
async def create_tables() -> None:
    print('Criando as tabelas no banco de dados...')

    # Criação das tabelas sem dependências (como AutorModel, TagModel, etc.)
    print('Criando tabelas sem dependências...')
    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.create_all, tables=[
            settings.DBBaseModel.metadata.tables['autores'],  # Exemplo: AutorModel
            settings.DBBaseModel.metadata.tables['tags'],  # Exemplo: TagModel
            settings.DBBaseModel.metadata.tables['areas'],  # Exemplo: AreaModel
        ])

    # Criação das tabelas associativas (tags_post, comentarios_post, tags_autor)
    print('Criando tabelas associativas (tags_post, comentarios_post, tags_autor)...')
    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.create_all, tables=[
            settings.DBBaseModel.metadata.tables['tags_post'],
            settings.DBBaseModel.metadata.tables['comentarios_post'],
            settings.DBBaseModel.metadata.tables['tags_autor'],  # Adicionando a tabela de associação
        ])

    # Criação das tabelas dependentes (como PostModel, ComentarioModel, DuvidaModel, ProjetoModel, MembroModel)
    print('Criando tabelas dependentes...')
    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.create_all, tables=[
            settings.DBBaseModel.metadata.tables['posts'],  # Exemplo: PostModel
            settings.DBBaseModel.metadata.tables['comentarios'],  # Exemplo: ComentarioModel
            settings.DBBaseModel.metadata.tables['duvidas'],  # Exemplo: DuvidaModel
            settings.DBBaseModel.metadata.tables['projetos'],  # Exemplo: ProjetoModel
            settings.DBBaseModel.metadata.tables['membros'],  # Exemplo: MembroModel
        ])

    print('Tabelas criadas com sucesso!')

