import os

from .base import * # noqa


DEBUG = True
ALLOWED_HOSTS = ['*']
DEV = DEBUG


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'practice_crud.db',
    }
}


SECRET_KEY = 'devel'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SITE_ID = 2

AUTH_PASSWORD_VALIDATORS = []