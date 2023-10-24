from typing import List

from fastapi import APIRouter
from fastapi import Depends

from ..models.user import User
from ..database import get_session
from ..services.user import UsersService
from .. import tables


router = APIRouter(
    prefix='/user'
)


@router.get('/', response_model=List[User])
def get_users_list(db: UsersService = Depends(get_session)):
    users = UsersService(db)
    return users.get_list(db)


@router.get('/{telegram_id}', response_model=User)
def get_separate_user(telegram_id: int, db: UsersService = Depends(get_session)):
    currency = UsersService(db)
    return currency.get_user(telegram_id, db)
