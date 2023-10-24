from typing import List

from sqlalchemy.orm import Session

from .. import tables
from ..tables import Currency


class CurrencyService:
    def __init__(self, db):
        self.db = db

    def get_list(self, db: Session) -> List[Currency]:
        return self.db.query(tables.Currency).all()
        # return self.db.query(tables.Currency).filter(tables.Currency.id == currency_id).first()

    def get_currency(self, currency_id: int, db: Session) -> Currency:
        return self.db.query(Currency).filter(Currency.id == currency_id).first()
