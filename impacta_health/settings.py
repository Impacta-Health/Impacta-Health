"""
Django settings for impacta_health project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path
import dj_database_url
from functools import partial
from decouple import Csv, config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())


# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
    # Apps
    "tasks",
    "about",
    "users",
    # Cleanup Media files Management
    "django_cleanup.apps.CleanupSelectedConfig",  # This should be placed in last position
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "impacta_health.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "impacta_health.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


default_db_url = 'sqlite:///' + os.path.join(BASE_DIR / 'db.sqlite3')
parse_database = partial(dj_database_url.parse, conn_max_age=600)
DATABASES = {
    'default': config('DATABASE_URL', default=default_db_url, cast=parse_database)
}

# Auth user
AUTH_USER_MODEL = "users.User"

AUTHENTICATION_BACKENDS = [
    "users.validators.custom_auth.CustomAuthenticationBackend",
    "django.contrib.auth.backends.ModelBackend",
]


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_URL = "/staticfiles/"

STATIC_URL = "/staticfiles/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

MEDIA_URL = "/mediafiles/"
MEDIA_ROOT = os.path.join(BASE_DIR, "mediafiles")

COLLECTFAST_ENABLE = False  # Development mode

if config("S3_ACCESS_KEY"):
    COLLECT_FAST_ENABLE = True
    AWS_ACCESS_KEY_ID = config("S3_ACCESS_KEY")
    AWS_SECRET_ACCESS_KEY = config("S3_SECRET_KEY")
    AWS_STORAGE_BUCKET_NAME = config("S3_BUCKET")
    AWS_S3_ENDPOINT_URL = config("S3_ENDPOINT")
    AWS_S3_OBJECT_PARAMETERS = {
        "CacheControl": "max-age=86400",
    }
    AWS_DEFAULT_ACL = "public-read"
    AWS_QUERYSTRING_AUTH = True
    AWS_S3_SIGNATURE_VERSION = "s3v4"
    MEDIA_CDN = config("MEDIA_CDN", default=AWS_S3_ENDPOINT_URL[8:])
    MEDIA_URL = "{}/{}/".format(MEDIA_CDN, AWS_STORAGE_BUCKET_NAME)
    MEDIA_ROOT = config("MEDIA_FOLDER", "")
    INSTALLED_APPS.append("collectfast")
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
    COLLECTFAST_STRATEGY = "collectfast.strategies.boto3.Boto3Strategy"


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Mail server configs
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
DOMAIN = config("DOMAIN")
EMAIL_HOST = config("EMAIL_HOST")
EMAIL_PORT = config("EMAIL_PORT")

if not DEBUG:
    EMAIL_HOST_USER = config("EMAIL_USERNAME")
    EMAIL_HOST_PASSWORD = config("EMAIL_PASSWORD")
    EMAIL_USE_TLS = True