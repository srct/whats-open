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
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

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

    Built-in query parameters:

    GET /api/facilities/?search=
    Query parameter that returns objects that match a keyword provided in the search.

    GET /api/facilities/?ordering=
    Query parameter that orders the returned objects based on the provided field to order by.

    Additionally, you can query against any field you like:

    ie.
    GET /api/facilities/?facility_name=Southside
    will return the Facility object that has "Southside" as its name.

    Custom query parameters:

    GET /api/facilities/?open_now
    Query parameter that only returns open Facility objects.

    GET /api/facilities/?closed_now
    Query parameter that only returns closed Facility objects.
    """
    # Associate a serializer with the ViewSet
    serializer_class = FacilitySerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter, )
    search_fields = ('facility_name',)
    ordering_fields = ('facility_name',)
    filter_fields = ('facility_name', 'facility_product_tags__name')

    def get_queryset(self):
        """
        Handle incoming GET requests and enumerate objects that get returned by
        the API.
        """
        # Define ?open_now
        open_now = self.request.query_params.get('open_now', None)
        # Define ?closed_now
        closed_now = self.request.query_params.get('closed_now', None)
        if open_now is not None or closed_now is not None:
            # List of all open facilities
            open_facilities = []
            for facility in Facility.objects.all():
                if facility.is_open():
                    # Append the primary key
                    open_facilities.append(facility.pk)
            # Return all Facility objects with the primary keys located in the
            # open_facilities list
            if open_now:
                return Facility.objects.filter(pk__in=open_facilities)
            # Return all Facility objects with the primary keys not located in
            # the open_facilities list
            elif closed_now:
                return Facility.objects.exclude(pk__in=open_facilities)
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