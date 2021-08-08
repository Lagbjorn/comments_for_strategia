from .base import *

DEBUG = True

INSTALLED_APPS.extend(
    [
        "debug_toolbar",
    ],
)

INTERNAL_IPS = [
    '127.0.0.1',
]

MIDDLEWARE.extend(
    [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ],
)

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: DEBUG
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },
    'formatters': {
        'default': {
            'format': '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]',
        },
    },
    'handlers': {
        'debug-console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'filters': ['require_debug_true'],
        },
    },
    'loggers': {
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['debug-console'],
            'propagate': False,
        }
    },
}
