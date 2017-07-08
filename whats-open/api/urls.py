"""
api/urls.py

Define the routes that the API will serve content through.

http://www.django-rest-framework.org/api-guide/routers/
"""
# Future Imports
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

# Django Imports
from django.conf.urls import include, url
from django.views.generic.base import RedirectView

# App Imports
from .views import (CategoryViewSet, FacilityViewSet, ScheduleViewSet,
                    LocationViewSet, AlertViewSet)

# Other Imports
from rest_framework.routers import DefaultRouter

# Instantiate our DefaultRouter
ROUTER = DefaultRouter()

# Register views to the API router
ROUTER.register(r'categories', CategoryViewSet, 'category')
ROUTER.register(r'facilities', FacilityViewSet, 'facility')
ROUTER.register(r'schedules', ScheduleViewSet, 'schedule')
ROUTER.register(r'locations', LocationViewSet, 'location')
ROUTER.register(r'alerts', AlertViewSet, 'alert')

urlpatterns = [
    # / - Default route
    # We redirect to /api since this is in reality the default page for the API
    url(r'^$', RedirectView.as_view(url='/api')),
    # /api - Root API URL
    url(r'^api/', include(ROUTER.urls)),
]
