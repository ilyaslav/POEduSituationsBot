from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from settings import settings

engine = create_async_engine(
    url = settings.DATABASE_URL,
    echo = False,
)

session_factory = async_sessionmaker(engine)