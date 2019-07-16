"""
Django settings for devnews project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
# built-in
import os

# third-party
from dotenv import load_dotenv

load_dotenv(verbose=True)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(__file__)
SETTINGS_PATH = os.path.dirname(__file__)
PROJECT_PATH = os.path.abspath(os.path.join(SETTINGS_PATH, os.pardir))
TEMPLATES_PATH = os.path.join(PROJECT_PATH, 'templates')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY') or 'sample-secret-key'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DJANGO_DEBUG') or True

if DEBUG:
    ALLOWED_HOSTS = ['*']  # in dev
else:
    ALLOWED_HOSTS = [ # in prod
        'devnews.kr',
    ]


# Application definition
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'django_extensions',
    'rest_framework',
    'admin_interface',
    'colorfield',
    'taggit',
)

LOCAL_APPS = (
    # 'api',
    'users',
    'links',

    # sentry raven
    # 'raven.contrib.django.raven_compat',
)

INSTALLED_APPS = THIRD_PARTY_APPS + DJANGO_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # third-party
]

ROOT_URLCONF = 'devnews.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'devnews.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': os.getenv('DJANGO_DB_HOST') or '127.0.0.1',
        'PORT': os.getenv('DJANGO_DB_PORT') or '3306',
        'NAME': os.getenv('DJANGO_DB_NAME') or 'devnews-db',
        'USER': os.getenv('DJANGO_DB_USERNAME') or 'devnews-user',
        'PASSWORD': os.getenv('DJANGO_DB_PASSWORD') or 'devnews-password',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
            'use_unicode': True,
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/assets/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'assets'),
    # os.path.join(PROJECT_DIR, 'staticfiles'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

ADMIN_MEDIA_ROOT = os.path.join(BASE_DIR, 'media/admin')
ADMIN_MEDIA_URL = '/media/admin/'

# AUTH_USER_MODEL = 'user.DefaultUser'
LOGIN_URL = '/login'
LOGIN_REDIRECT_URL = '/admin'
LOGIN_ERROR_URL = '/login'
LOGOUT_URL = '/logout'
LOGOUT_REDIRECT_URL = '/login'

# third-party options
IMPORT_EXPORT_USE_TRANSACTIONS = True
TAGGIT_CASE_INSENSITIVE = True

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
}
