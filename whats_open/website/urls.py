# Future Imports
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

# Django Imports
from django.conf.urls import include, url

# App Imports
from .views import CategoryViewSet, FacilityViewSet, ScheduleViewSet

# Other Imports
from rest_framework.routers import DefaultRouter

# Instiantiate our DefaultRouter
ROUTER = DefaultRouter()

# Register views to the API router
ROUTER.register(r'categories', CategoryViewSet)
ROUTER.register(r'facilities', FacilityViewSet)
ROUTER.register(r'schedules', ScheduleViewSet)

urlpatterns = [
    # /api - Root API URL
    url(r'^api/', include(ROUTER.urls)),
]
