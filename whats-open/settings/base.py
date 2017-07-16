""""
settings/base.py

Base Django settings for whats-open.
"""
# Future Imports
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

# Python std. lib. imports
import os
import sys
from os.path import abspath, dirname, join, normpath
from sys import path

"""
PATH CONFIGURATION
"""
# Absolute filesystem path to the Django project directory:
DJANGO_ROOT = dirname(dirname(abspath(__file__)))

# Absolute filesystem path to the top-level project folder:
SITE_ROOT = dirname(DJANGO_ROOT)

# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(DJANGO_ROOT)

"""
MANAGER CONFIGURATION
"""
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
# Insert a ('Name', 'Email') inside ADMINS tuple
ADMINS = (
    ('SRCT Admin', 'srct@gmu.edu'),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS

"""
GENERAL CONFIGURATION
"""
# See: https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/New_York'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

"""
MEDIA CONFIGURATION
"""
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = normpath(join(SITE_ROOT, 'media'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

"""
STATIC FILE CONFIGURATION
"""
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = normpath(join(SITE_ROOT, 'static'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/static/admin/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

"""
SECRET CONFIGURATION
"""
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key should only be used for development and testing.
SECRET_KEY = r"{{ secret_key }}"

"""
SITE CONFIGURATION
"""
# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']
########## END SITE CONFIGURATION


"""
FIXTURE CONFIGURATION
"""
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
    normpath(join(SITE_ROOT, 'fixtures')),
)

"""
DATABASE CONFIGURATION
"""
# Use the same DB everywhere.
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.mysql',
        'NAME': os.environ['WOPEN_DB_NAME'],
        'USER': os.environ['WOPEN_DB_USER'],
        'PASSWORD': os.environ['WOPEN_DB_PASSWORD'],
        'HOST': os.environ['WOPEN_DB_HOST'],
        'PORT': os.environ['WOPEN_DB_PORT'],
    }
}

"""
TEMPLATE CONFIGURATION
"""
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
        'DIRS': [
            normpath(join(SITE_ROOT, 'templates'))
        ],
        'OPTIONS': {
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
        }
    }
]

"""
MIDDLEWARE CONFIGURATION
"""
# See: https://docs.djangoproject.com/en/dev/ref/settings/#middleware-classes
MIDDLEWARE_CLASSES = (
    # Default Django middleware.
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

"""
URL CONFIGURATION
"""
# See: https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = 'settings.urls'

"""
WSGI CONFIGURATION
"""
# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'settings.wsgi.application'

"""
SERIALIZER CONFIGURATION
"""
# http://djx.readthedocs.org/en/latest/topics/http/sessions.html#session-serialization
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

"""
CACHE MIDDLEWARE CONFIGURATION
"""
CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = 259200
CACHE_MIDDLEWARE_KEY_PREFIX = ''

"""
APP CONFIGURATION
"""
INSTALLED_APPS = (
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Admin panel and documentation:
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.gis',

    # Apps specific for this project go here.
    'api',

    # Third party apps
    'taggit',
    'taggit_serializer',
    'rest_framework',
    'rest_framework_gis',
    'django_filters',
    'crispy_forms',
)

"""
DJANGO REST FRAMEWORK CONFIGURATION
"""
# http://www.django-rest-framework.org/api-guide/settings
REST_FRAMEWORK = {
    # Use hyperlinked styles by default.
    # Only used if the `serializer_class` attribute is not set on a view.
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.HyperlinkedModelSerializer',

    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

"""
LOGGING CONFIGURATION
"""
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propogate': True
        },
    }
}
