# Future Imports
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

# Django Imports
from django.conf.urls import include, url
from django.views.generic.base import RedirectView

# App Imports
from .views import CategoryViewSet, FacilityViewSet, ScheduleViewSet

# Other Imports
from rest_framework.routers import DefaultRouter

# Instantiate our DefaultRouter
ROUTER = DefaultRouter()

# Register views to the API router
ROUTER.register(r'categories', CategoryViewSet)
ROUTER.register(r'facilities', FacilityViewSet)
ROUTER.register(r'schedules', ScheduleViewSet)

urlpatterns = [
    # / - Default route
    # We redirect to /api since this is in reality the default page for the API
    url(r'^$', RedirectView.as_view(url='/api')),
    # /api - Root API URL
    url(r'^api/', include(ROUTER.urls)),
]
