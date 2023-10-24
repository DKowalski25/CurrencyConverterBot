import sqlalchemy as sa
from datetime import datetime

from .database import engine, Base


# Table representing the telegram user
class User(Base):
    __tablename__ = 'users'

    telegram_id = sa.Column(sa.Integer, primary_key=True)
    user_name = sa.Column(sa.String)
    lang_code = sa.Column(sa.String)
    first_name = sa.Column(sa.String)
    last_name = sa.Column(sa.String)
    registration_date = sa.Column(sa.DateTime)
    country = sa.Column(sa.String)


    # telegram_id: str
    # user_name: str
    # lang_code: str
    # first_name: Optional[str]
    # last_name: Optional[str]


# Table representing the all currency
class Currency(Base):
    __tablename__ = 'currency'

    id = sa.Column(sa.Integer, primary_key=True)
    currency_name = sa.Column(sa.String)


Base.metadata.create_all(bind=engine)
