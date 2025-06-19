import logging
import logging.config
from config.logging.logging_settings import LOGGING_CONFIG
from functools import lru_cache
from config.settings import Settings


@lru_cache()
def load_logger():
    """Load and configure the logger based on settings."""
    settings = Settings.load()
    logging.config.dictConfig(LOGGING_CONFIG)
    logger = logging.getLogger(settings.LOGGER_NAME)
    return logger


