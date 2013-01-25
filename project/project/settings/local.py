from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

SOUTH_TESTS_MIGRATE = False
SOUTH_DATABASE_ADAPTER='south.db.psycopg2'
SKIP_SOUTH_TESTS = True
