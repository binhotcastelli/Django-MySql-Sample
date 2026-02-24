import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / '.env')

def get_env(name):
    value = os.getenv(name)
    if not value:
        raise Exception(f'Variável de ambiente {name} não definida.')
    return value

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': get_env('MYSQL_DB'),
        'USER': get_env('MYSQL_USER'),
        'PASSWORD': get_env('MYSQL_PASSWORD'),
        'HOST': get_env('MYSQL_HOST'),
        'PORT': get_env('MYSQL_PORT'),
    }
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'apps.users',
]