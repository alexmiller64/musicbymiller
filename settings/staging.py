from base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_bGSY225Gxzy1kMzKpXYgnM4d')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_uCphKUt2PziPqiNBYxbFn6Hi')

SITE_URL = 'https://sixsalt.herokuapp.com'
ALLOWED_HOSTS.append('sixsalt.herokuapp.com')

# Log DEBUG information to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}
