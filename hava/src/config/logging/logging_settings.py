from config.logging.formatter.custom_json_formatter import CustomJSONFormatter
from config.settings import Settings


settings = Settings.load()

LOGGING_CONFIG = { 
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': { 
        'standard': { 
            'format': settings.LOG_FORMAT,
        },
        'custom_json_formatter': { 
            '()':  lambda: CustomJSONFormatter(fmt='%(asctime)s')           
        },
        'custom_formatter': { 
            'format': settings.LOG_FORMAT,  
        },
    },
    'handlers': { 
        'default': { 
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',  # Default is stderr
        },
        'stream_handler': { 
            'formatter': 'custom_formatter',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',  # Default is stderr
        },
        'file_handler': { 
            'formatter': 'custom_json_formatter',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': settings.LOG_FILE,  # Default log file name
            'maxBytes': settings.LOG_MAX_BYTES, # = 1MB
            'backupCount': settings.LOG_BACKUP_COUNT,  # Number of backup log files to keep
        },
    },
    'loggers': {
        f'{settings.LOGGER_NAME}': {
            'handlers': ['default', 'file_handler'],
            'level': 'INFO', 
            'propagate': False
        },
        # 'uvicorn': {
        #     'handlers': ['default', 'file_handler'],
        #     'level': 'TRACE',
        #     'propagate': False
        # },
        # 'uvicorn.access': {
        #     'handlers': ['stream_handler', 'file_handler'],
        #     'level': 'TRACE',
        #     'propagate': False
        # },
        # 'uvicorn.error': { 
        #     'handlers': ['stream_handler', 'file_handler'],
        #     'level': 'TRACE',
        #     'propagate': False
        # },
        # 'uvicorn.asgi': {
        #     'handlers': ['stream_handler', 'file_handler'],
        #     'level': 'TRACE',
        #     'propagate': False
        # },
    },
}
