from typing import List

from sqlalchemy.orm import Session

from .. import tables
from ..tables import User


class UsersService:
    def __init__(self, db):
        self.db = db

    def get_list(self, db: Session) -> List[User]:
        return self.db.query(tables.User).all()
        # return self.db.query(tables.Currency).filter(tables.Currency.id == currency_id).first()

    def get_user(self, telegram_id: int, db: Session) -> User:
        return self.db.query(User).filter(User.telegram_id == telegram_id).first()
