"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.10.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'cs0s!8_-)*5foq1ffet1^##2e583r!j%#wng3fcl8sm5jln1xu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'photologue',
    'sortedm2m',
    'contact_form',
]

SITE_ID = 1

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'PAGINAWEB1.urls'

CONTACT_FORM_RECIPIENTS = (
    ('daysi fernandez', 'dfdtex@gmail.com'),
)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'PAGINAWEB1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'es_AR'

TIME_ZONE = 'America/La_Paz'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'public', 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'public', 'media')
MEDIA_URL = '/media/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


# LOGGING CONFIGURATION
# A logging configuration that writes log messages to the console.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    # Formatting of messages.
    'formatters': {
        # Don't need to show the time when logging to console.
        'console': {
            'format': '%(levelname)s %(name)s.%(funcName)s (%(lineno)d) %(message)s'
        }
    },
    # The handlers decide what we should do with a logging message - do we email
    # it, ditch it, or write it to a file?
    'handlers': {
        # Writing to console. Use only in dev.
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        },
        # Send logs to /dev/null.
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
    },
    # Loggers decide what is logged.
    'loggers': {
        '': {
            # Default (suitable for dev) is to log to console.
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'photologue': {
            # Default (suitable for dev) is to log to console.
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        # logging of SQL statements. Default is to ditch them (send them to
        # null). Note that this logger only works if DEBUG = True.
        'django.db.backends': {
            'handlers': ['null'],
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}

# Don't display logging messages to console during unit test runs.
if len(sys.argv) > 1 and sys.argv[1] == 'test':
    LOGGING['loggers']['']['handlers'] = ['null']
    LOGGING['loggers']['photologue']['handlers'] = ['null']

# Uncomment this for Amazon S3 file storage
# from example_storages.settings_s3boto import *
