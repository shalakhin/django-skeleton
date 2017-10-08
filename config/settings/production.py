from ._base import *
from urlparse import urlparse
import dj_database_url

DEBUG = False

DATABASES = {}
DATABASES['default'] = dj_database_url.config()

MIDDLEWARE_CLASSES = (
    'johnny.middleware.LocalStoreClearMiddleware',
    'johnny.middleware.QueryCacheMiddleware',
) + MIDDLEWARE_CLASSES

INSTALLED_APPS = (
    'raven.contrib.django.raven_compat',
) + INSTALLED_APPS

redis_url = urlparse(os.environ['REDISTOGO_URL'])

CACHES = {
    'default': {
        'BACKEND': 'johnny.backends.redis.RedisCache',
        'LOCATION': '%s:%s' % (redis_url.hostname, redis_url.port),
        'JOHNNY_CACHE': True,
        'OPTIONS': {
            'DB': 0,
            'PASSWORD': redis_url.password
        }
    }
}
