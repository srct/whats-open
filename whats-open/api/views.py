"""
api/views.py

Rest Framework Class Views
"""
# Future Imports
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

# Python std. lib. imports
import datetime

# App Imports
from .models import Facility, OpenTime, Category, Schedule, Location, Alert
from .serializers import (CategorySerializer, FacilitySerializer,
                          ScheduleSerializer, OpenTimeSerializer,
                          LocationSerializer, AlertSerializer)

# Other Imports
from rest_framework import viewsets

class AlertViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Return all Alert objects.
    """
    serializer_class = AlertSerializer

    def get_queryset(self):
        """
        Handle incoming GET requests and enumerate objects that get returned by
        the API.
        """
        return Alert.objects.all()

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Return all Category objects.
    """
    serializer_class = CategorySerializer

    def get_queryset(self):
        """
        Handle incoming GET requests and enumerate objects that get returned by
        the API.
        """
        return Category.objects.all()

class LocationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Return all Location objects.
    """
    serializer_class = LocationSerializer

    def get_queryset(self):
        """
        Handle incoming GET requests and enumerate objects that get returned by
        the API.
        """
        return Location.objects.all()

class FacilityViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A Facility is some type of establishment that has a schedule of open hours and a location that serves a specific purpose that can be categorized.

    GET /api/facilities/
    Return all Facility objects. We additionally filter out stale special_schedules to reduce client side calculations.

    GET /api/facilities/?open_now
    Query parameter that only returns open Facility objects.
    """
    serializer_class = FacilitySerializer

    def get_queryset(self):
        """
        Handle incoming GET requests and enumerate objects that get returned by
        the API.
        """
        # Define and handle ?open_now
        open_now = self.request.query_params.get('open_now', None)
        if open_now is not None:
            # List of all open facilities
            open_facilities = []
            for facility in Facility.objects.all():
                if facility.is_open():
                    # Append the primary key
                    open_facilities.append(facility.pk)
            # Return all Facility objects with the primary keys located in the
            # open_facilities list
            return Facility.objects.filter(pk__in=open_facilities)
        # Default behavior
        else:
            for facility in Facility.objects.all():
                # Remove all special_schedules that have expired
                facility.clean_special_schedules()
            return Facility.objects.all()

class ScheduleViewSet(viewsets.ModelViewSet):
    """
    A period of time between two dates that represents the beginning and end of a "schedule" or rather, a collection of open times for a facility.

    GET /api/schedules
    Return all Schedule objects that have not expired. (ie. end_date is before today)
    """
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        """
        Handle incoming GET requests and enumerate objects that get returned by
        the API.
        """
        # List of all schedules that are outdated
        filter_old_schedules = []
        for schedule in Schedule.objects.all():
            if schedule.valid_end and schedule.valid_start:
                # If the schedule ended before today
                if schedule.valid_end < datetime.date.today():
                    # Add it to the list of objects we are excluding
                    filter_old_schedules.append(schedule.pk)
        # Return all Schedule objects that have not expired
        return Schedule.objects.exclude(pk__in=filter_old_schedules)

class OpenTimeViewSet(viewsets.ModelViewSet):
    """
    Return all OpenTime objects.
    """
    serializer_class = OpenTimeSerializer

    def get_queryset(self):
        """
        Handle incoming GET requests and enumerate objects that get returned by
        the API.
        """
        return OpenTime.objects.all()