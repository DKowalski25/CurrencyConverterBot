from pydantic import BaseModel


class Currency(BaseModel):
    id: int
    currency_name: str
