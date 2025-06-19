import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from core.dependencies import get_settings, get_logger
from config.logging.logging_settings import LOGGING_CONFIG
from core.api import router as api_router

settings = get_settings()
logger = get_logger()
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=settings.APP_DESCRIPTION)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(api_router, prefix=settings.API_PATH)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        description=settings.APP_DESCRIPTION,
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

if __name__ == "__main__":
    logger.info(f"Starting {settings.APP_NAME} on port {settings.HTTP_PORT}")
    reload = not settings.is_production
    uvicorn.run(app, log_config=LOGGING_CONFIG, workers=4, host="127.0.0.1", port=settings.HTTP_PORT, reload=reload)
