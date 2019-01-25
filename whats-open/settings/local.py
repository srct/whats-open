#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
settings/local.py

Development settings and globals.
"""
# Import the base settings and override where necessary
from .base import *

"""
DEBUG CONFIGURATION
"""
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

"""
CACHE CONFIGURATION
"""
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {"default": {"BACKEND": "django.core.cache.backends.locmem.LocMemCache"}}
