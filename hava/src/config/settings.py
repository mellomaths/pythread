from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        case_sensitive=True,
        extra='ignore'
    )
    
    PY_ENV: str = 'local'  # Environment type (local, dev, prod)

    # Application settings
    APP_NAME: str = 'Hava API'
    APP_VERSION: str = '0.0.1'
    APP_DESCRIPTION: str = 'A platform for lovers to share their experiences'
    API_NAME: str = 'hava'
    API_VERSION: str = 'v1'
    API_PATH: str = f'/{API_NAME}/api/{API_VERSION}'
    
    # Server settings
    HTTP_PORT: int = 8000
    
    # Feature flags
    RATING_TYPES: set = {"wine", "beer"}  # Supported rating types
    ENABLE_RATINGS: bool = True  # Enable or disable ratings feature
    ENABLE_WINES: bool = True  # Enable or disable wines feature
    ENABLE_BEERS: bool = True  # Enable or disable beers feature
    
    # Logging settings
    LOGGER_NAME: str = 'hava_api'
    LOG_LEVEL: str = 'TRACE'  # Default log level
    LOG_FORMAT: str = '%(asctime)s [%(processName)s: %(process)d] [%(threadName)s: %(thread)d] [%(levelname)s] %(name)s: %(message)s'
    LOG_FILE: str = 'app.log'  # Default log file name
    LOG_MAX_BYTES: int = 10485760  # 10 MB
    LOG_BACKUP_COUNT: int = 5  # Number of backup log files to keep
    
    # Database settings
    DATABASE_DIALECT: str = 'postgresql+psycopg2'  # Database type (e.g., postgresql+psycopg2, mysql+pymysql, sqlite)
    DATABASE_HOST: str = 'localhost'
    DATABASE_PORT: int = 5432
    DATABASE_USER: str = 'user'
    DATABASE_PASSWORD: str = 'password'
    DATABASE_NAME: str = 'database'
    DATABASE_URL: str = f'{DATABASE_DIALECT}://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}'
    
    # CORS settings
    CORS_ORIGINS: list[str] = ['*']  # Allow all origins by default
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: list[str] = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'] # Allow common HTTP methods
    
    @property
    def is_production(self) -> bool:
        return self.PY_ENV.lower() == 'prod'
    
    @staticmethod
    @lru_cache()
    def load():
        return Settings()


