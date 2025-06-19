from logging import Logger
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from core.dependencies import get_logger, get_database_session
from core.database import check_database_health
from core.health.model.health_check_model import HealthCheck


router = APIRouter()


@router.get('/', status_code=status.HTTP_200_OK, response_model=HealthCheck, responses={503: {"model": HealthCheck}})
def health_check(db_session: Session = Depends(get_database_session), logger: Logger = Depends(get_logger)):
    logger = logger.getChild('health_check_controller')
    logger.info('Retrieving Health Check')
    is_database_up, err_message = check_database_health(db_session)
    status_code = status.HTTP_200_OK
    is_database_up = True
    if not is_database_up:
        logger.error('Error on connecting to Database')
        logger.error(err_message)
        status_code = status.HTTP_503_SERVICE_UNAVAILABLE
    health = is_database_up
    if not health:
        logger.error('Health check failed')
        status_code = status.HTTP_503_SERVICE_UNAVAILABLE
    response  = { 'success': health, 'up': { 'database': is_database_up } }
    logger.info(f'Health check response: {response}')
    return JSONResponse(content=response, status_code=status_code)
