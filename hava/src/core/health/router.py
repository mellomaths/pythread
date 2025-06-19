from fastapi import APIRouter

import core.health.controller.health_check_controller as health_check

router = APIRouter()

router.include_router(health_check.router, prefix='/health', tags=['health'])
