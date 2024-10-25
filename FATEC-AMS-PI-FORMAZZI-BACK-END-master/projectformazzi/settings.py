import os
from pathlib import Path
from urllib.parse import quote_plus

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key, debug, and allowed hosts settings
SECRET_KEY = 'django-insecure-9!%uj)6tsr+0q8-ev+=!7wee)+m(5q)m*atic=$g*_9w5e1_zd'
DEBUG = True
ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [#esse bloco de comando serve para você definir os modulos e configs abaixo temos marcações de onde e provaveis nomeclaturas dos modulos futuros
    #''#certificados
    #''#prova
    #''#curso
    #''#funcionario
    'adm',
    #''#empresa
    'projectformazzi',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'djongo',
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

ROOT_URLCONF = 'projectformazzi.urls'

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

WSGI_APPLICATION = 'projectformazzi.wsgi.application'

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'FORMAZZI',
        'CLIENT': {
            'host': 'mongodb+srv://henricanosa:formazzi2024@cluster0.8vllj.mongodb.net/nome_do_banco_de_dados?retryWrites=true&w=majority',
            'tls': True,
            'tlsAllowInvalidCertificates': True,
        }
    }
}

# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = 'static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
