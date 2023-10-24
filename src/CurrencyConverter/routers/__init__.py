from fastapi import APIRouter

from .currency import router as currency_router
from .user import router as user_router

router = APIRouter()
router.include_router(currency_router)
router.include_router(user_router)
