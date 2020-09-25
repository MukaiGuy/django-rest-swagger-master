"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import environ

APP_NAME = 'Django Rest Swagger Master'

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# reading .env file
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG')

ALLOWED_HOSTS = []


MODE = 'TEMPLATE' # 'TEMPLATE' or 'REST'

if MODE == 'TEMPLATE':
    EXTENDED_INSTALLED_APPS = ['myapp.apps.MyappConfig']
    EXTENDED_MIDDLEWARE = []
    EXTENDED_CONTEXT_PROCESSORS = ['myapp.context_processors.context_processors']
    AUTH_USER_MODEL = 'myapp.User'

if MODE == 'REST':
    EXTENDED_INSTALLED_APPS = [
        'rest_framework',
        'rest_framework.authtoken',
        'rest_framework_swagger',
        'corsheaders',
        'api_v1.apps.MyappConfig',
    ]
    EXTENDED_MIDDLEWARE = ['corsheaders.middleware.CorsMiddleware']
    EXTENDED_CONTEXT_PROCESSORS = []
    AUTH_USER_MODEL = 'api_v1.User'
    REST_FRAMEWORK = {
        'PAGE_SIZE': 10,
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
        'DEFAULT_AUTHENTICATION_CLASSES': [
            'rest_framework.authentication.TokenAuthentication',
            'rest_framework.authentication.SessionAuthentication',
        ]
    }
    SWAGGER_SETTINGS = {
        'LOGIN_URL': 'rest_framework:login',
        'LOGOUT_URL': 'rest_framework:logout',
        'DOC_EXPANSION': 'list',
    }
    CORS_ORIGIN_WHITELIST = ["http://localhost:8080"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
] + EXTENDED_INSTALLED_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
] + EXTENDED_MIDDLEWARE

ROOT_URLCONF = 'mysite.urls'

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
            ] + EXTENDED_CONTEXT_PROCESSORS,
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    # 'mysql': env.db(),
    # 'postgresql': env.db(),
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = '{}/staticfiles'.format(BASE_DIR)

MEDIA_URL = '/media/'

MEDIA_ROOT = '{}/mediafiles'.format(BASE_DIR)