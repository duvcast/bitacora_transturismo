"""
Django settings for bitacora project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
# import sys
from pathlib import Path

# import dj_database_url
# from django.core.management.utils import get_random_secret_key

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from django.urls import reverse

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "qevma4a-m0yp^a1jbei-j@-(ltq1^91eozqm#o)ptcctb=eff#"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = "True"

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third party apis
    'tempus_dominus',
    'widget_tweaks',
    'django_htmx',

    # Local apps
    'main.apps.MainConfig',
    'users.apps.UsersConfig',
    'contratos.apps.ContratosConfig',
    'services.apps.ServicesConfig',
    'administremos.apps.AdministremosConfig',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bitacora.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'bitacora.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'transturismo',
        # 'NAME': 'juadznqy',
        # 'NAME': 'transturismo',
        'USER': 'doadmin',
        # 'USER': 'melius',
        # 'USER': 'juadznqy',
        # 'HOST': 'localhost',
        # 'HOST': 'tuffi.db.elephantsql.com',
        'HOST': 'db-postgresql-sfo3-transturismo-do-user-4477223-0.b.db.ondigitalocean.com',
        # 'HOST': 'private-db-postgresql-sfo3-transturismo-do-user-4477223-0.b.db.ondigitalocean.com',
        'PORT': '25060',
        # 'PORT': '5432',
        # 'PASSWORD': 'amunozro8970',
        # 'PASSWORD': '0tvUjzhaPc3Zk4giMHLCKei-ysVYWLo1'
        'PASSWORD': 'irrunras87percbh'
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = "users.User"

# widget hour
TEMPUS_DOMINUS_LOCALIZE = True
TEMPUS_DOMINUS_TIME_FORMAT = 'HH:mm'

LOGIN_REDIRECT_URL = "/contracts/spreadsheet/"
LOGIN_URL = "/login/"
LOGOUT_REDIRECT_URL = "/login/"
