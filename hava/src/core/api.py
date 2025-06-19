from fastapi import APIRouter

from core.health.router import router as health

router = APIRouter()

router.include_router(health)
