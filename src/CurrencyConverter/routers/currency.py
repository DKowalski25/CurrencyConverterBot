from typing import List

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from .. import tables
from ..database import get_session
from ..models.currency import Currency

router = APIRouter(
    prefix='/currency'
)


@router.get('/', response_model=List[Currency])
def get_currency(db: Session = Depends(get_session)):
    return db.query(tables.Currency).all()


# @app.get("/users/", response_model=list[schemas.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users