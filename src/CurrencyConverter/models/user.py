from typing import Optional
from datetime import datetime

from pydantic import BaseModel


class User(BaseModel):
    telegram_id: int
    user_name: str
    lang_code: str
    first_name: Optional[str]
    last_name: Optional[str]
    registration_date: datetime
    country: str

    class Config:
        orm_mode = True


# class UserCreate(User):
#     password: str

