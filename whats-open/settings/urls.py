#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
settings/urls.py

Top level url patterns.
"""
# Django Imports
from django.urls import include, path
from django.contrib import admin
import django.contrib.auth.views

# Automatically populate the admin pages
admin.autodiscover()

# Define all the top level url patterns in a list
urlpatterns = [
    # / - Load in all urls from the `api` app
    path('', include('api.urls')),

    # /admin/docs - Documentation for admin
    path('admin/doc/', include('django.contrib.admindocs.urls')),

    # /admin - The admin panels
    path('admin/', admin.site.urls),

    # /api-auth - API Auth page
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # /logout - Redirect to the homepage on logout
    path('logout/', django.contrib.auth.views.logout, {'next_page': '/'}),
]
