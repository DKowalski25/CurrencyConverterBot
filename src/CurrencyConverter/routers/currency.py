from typing import List

from fastapi import APIRouter
from fastapi import Depends


from ..models.currency import Currency
from ..services.currency import CurrencyService
from ..database import get_session


router = APIRouter(
    prefix='/currency'
)


@router.get('/', response_model=List[Currency])
def get_currency_list(db: CurrencyService = Depends(get_session)):
    currencies = CurrencyService(db)
    return currencies.get_list(db)


@router.get('/{currency_id}', response_model=Currency)
def get_currency(currency_id: int, db: CurrencyService = Depends(get_session)):
    currency = CurrencyService(db)
    return currency.get_currency(currency_id, db)











