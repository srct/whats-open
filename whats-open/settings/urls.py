"""
settings/urls.py

Top level url patterns.
"""
# Future Imports
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

# Django Imports
from django.conf.urls import include, url
from django.contrib import admin
import django.contrib.auth.views

# Automatically populate the admin pages
admin.autodiscover()

# Define all the top level url patterns in a list
urlpatterns = [
    # / - Load in all urls from the `api` app
    url(r'^', include('api.urls')),

    # /admin - The admin panels
    url(r'^admin/', include(admin.site.urls)),

    # /admin/docs - Documentation for admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # /api-auth - API Auth page
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # /logout - Redirect to the homepage on logout
    url(r'^logout/$', django.contrib.auth.views.logout, {'next_page': '/'}),
]
