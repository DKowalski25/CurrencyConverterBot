from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


from .settings import settings

engine = create_engine(
    settings.database_url,
    # echo=True,
    # pool_size=5,
    # max_overflow=10,
)


Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session() -> Session:
    session = Session()
    try:
        yield session
    finally:
        session.close()


Base = declarative_base()