#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
settings/production.py

Production settings and globals.
"""
# Python std. lib imports
from os import environ

# Django Imports
from django.core.exceptions import ImproperlyConfigured

# Import the base settings and override where necessary
from .base import *

def get_env_setting(setting):
    """
    Get the environment setting or return exception
    """
    try:
        return environ[setting]
    except KeyError as ex:
        print(str(ex))
        error_msg = "Set the %s env variable" % setting
        raise ImproperlyConfigured(error_msg)

"""
HOST CONFIGURATION
"""
# See: https://docs.djangoproject.com/en/1.5/releases/1.5/#allowed-hosts-required-in-production
ALLOWED_HOSTS = ['*']

"""
DEBUG CONFIGURATION
"""
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False

"""
CACHE CONFIGURATION
"""
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

"""
SECRET CONFIGURATION
"""
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = get_env_setting('WOPEN_SECRET_KEY')
########## END SECRET CONFIGURATION
