from settings_base import *

ENVIRONMENT = 'PROD'

DEBUG = False
TEMPLATE_DEBUG = DEBUG
DAJAXICE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'lisean_personal',
        'USER': 'lisean_personal',
        'PASSWORD': '1990106',
        'HOST': '',
        'PORT': '',
    }
}

STATIC_ROOT = '/home/lisean/webapps/lisean_static/'
STATIC_URL = 'http://lisean.com/static/'
MEDIA_ROOT = '/home/lisean/webapps/lisean_media/'
MEDIA_URL = 'http://lisean.com/media/'

COMPRESS_ENABLED = True
