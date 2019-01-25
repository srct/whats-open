#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
api/urls.py

Define the routes that the API will serve content through.

http://www.django-rest-framework.org/api-guide/routers/
"""
# Django Imports
from django.urls import include, path
from django.views.generic.base import RedirectView

# App Imports
from .views import (
    CategoryViewSet,
    FacilityViewSet,
    ScheduleViewSet,
    LocationViewSet,
    AlertViewSet,
)

# Other Imports
from rest_framework.routers import DefaultRouter

# Instantiate our DefaultRouter
ROUTER = DefaultRouter()

# Register views to the API router
ROUTER.register(r"alerts", AlertViewSet, "alert")
ROUTER.register(r"categories", CategoryViewSet, "category")
ROUTER.register(r"facilities", FacilityViewSet, "facility")
ROUTER.register(r"locations", LocationViewSet, "location")
ROUTER.register(r"schedules", ScheduleViewSet, "schedule")

urlpatterns = [
    # / - Default route
    # We redirect to /api since this is in reality the default page for the API
    path("", RedirectView.as_view(url="/api")),
    # /api - Root API URL
    path("api/", include(ROUTER.urls)),
]
