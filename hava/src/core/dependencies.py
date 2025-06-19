from config.logging.logger import load_logger
from config.settings import Settings
from core.database import SessionLocal


def get_database_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
def get_settings():
    settings = Settings.load()
    if not settings:
        raise ValueError("Settings could not be loaded")
    return settings


def get_logger():
    return load_logger()
