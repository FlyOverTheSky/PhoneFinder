import os.path
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-klnajf*1zk)$#a+8i#)m89a0ra%z&po!xe&xx@0!g&=_@#_&y&'

DEBUG = True

ALLOWED_HOSTS = []


DOWNLOAD_URLS = {
    '3xx': 'https://opendata.digital.gov.ru/downloads/ABC-3xx.csv',
    '4xx': 'https://opendata.digital.gov.ru/downloads/ABC-4xx.csv',
    '8xx': 'https://opendata.digital.gov.ru/downloads/ABC-8xx.csv',
    '9xx': 'https://opendata.digital.gov.ru/downloads/DEF-9xx.csv',
}

DB_DETAILS = {
    'database': 'postgres',
    'user': 'user',
    'password': 'user',
    'host': 'localhost',
    'port': 5432
}

TABLE_NAMES = [
    "3xx",
    "4xx",
    "8xx",
    "9xx"
]
CSVS_FOLDER_NAME = 'csvs'
CSVS_PATH = os.path.join(BASE_DIR, 'phone_finder', CSVS_FOLDER_NAME)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'phone_finder.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'phone_finder.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
