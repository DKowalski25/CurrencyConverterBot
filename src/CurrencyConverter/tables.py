import sqlalchemy as sa

from .database import engine, Base


class Currency(Base):
    __tablename__ = 'currency'

    id = sa.Column(sa.Integer, primary_key=True)
    currency_name = sa.Column(sa.String)


Base.metadata.create_all(bind=engine)
