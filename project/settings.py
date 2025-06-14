import os

import dj_database_url
from environs import env


env.read_env()
SECRET_KEY = env('SECRET_KEY')
DB_URL = env('DB_URL')
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS')
DEBUG = env.bool('DEBAG', default=False)

DATABASES = {
    'default': dj_database_url.config(default=DB_URL)
}

INSTALLED_APPS = ['datacenter']

ROOT_URLCONF = 'project.urls'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
