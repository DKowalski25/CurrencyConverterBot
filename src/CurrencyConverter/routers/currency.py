from fastapi import APIRouter
from fastapi import Depends


from ..models.currency import Currency
from ..services.currency import CurrencyService
from ..database import get_session


router = APIRouter(
    prefix='/currency'
)


@router.get('/', response_model=list[Currency])
def get_currency(db: CurrencyService = Depends(get_session)):
    currencies = CurrencyService(db)
    return currencies.get_list(db)










