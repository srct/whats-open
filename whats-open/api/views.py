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
    Some type of notification that is displayed to clients that conveys a message.

    Past examples include:
        - random closings
        - modified schedules being in effect
        - election reminder
        - advertising for other SRCT projects

    Alerts last for a period of time until the information is no longer dank.

    GET /api/alerts/
    Return all Alert objects.

    Built-in query parameters:

    GET /api/alerts/?search=
    Query parameter that returns objects that match a keyword provided in the search.

    GET /api/alerts/?ordering=
    Query parameter that orders the returned objects based on the provided field to order by.

    Additionally, you can query against any field you like:

    ie.
    GET /api/alerts/?urgency_tag=major
    will return the Alert objects that are tagged as "major" urgency.
    """
    # All model fields that are available for filtering
    FILTER_FIELDS = (
        # Alert fields
        'urgency_tag',
        'message',
        'start_datetime',
        'end_datetime'
    )

    # Associate a serializer with the ViewSet
    serializer_class = AlertSerializer

    # Setup filtering
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,
                       filters.OrderingFilter, )
    search_fields = FILTER_FIELDS
    ordering_fields = FILTER_FIELDS
    filter_fields = FILTER_FIELDS

    def get_queryset(self):
        """
        Handle incoming GET requests and enumerate objects that get returned by
        the API.
        """
        return Alert.objects.all()

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A Category is a grouping of Facilities that serve a common/similar purpose.

    ex.
        - Dining
        - Gyms
        - Study areas (Libraries, The Ridge, JC, etc)

    GET /api/categories/
    Return all Category objects.

    Built-in query parameters:

    GET /api/categories/?search=
    Query parameter that returns objects that match a keyword provided in the search.

    GET /api/categories/?ordering=
    Query parameter that orders the returned objects based on the provided field to order by.

    Additionally, you can query against any field you like:

    ie.
    GET /api/categories/?name=dining
    will return the Category object that is named "dining".
    """
    # All model fields that are available for filtering
    FILTER_FIELDS = (
        # Category fields
        'name',
    )

    # Associate a serializer with the ViewSet
    serializer_class = CategorySerializer

    # Setup filtering
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,
                       filters.OrderingFilter, )
    search_fields = FILTER_FIELDS
    ordering_fields = FILTER_FIELDS
    filter_fields = FILTER_FIELDS

    def get_queryset(self):
        """
        Handle incoming GET requests and enumerate objects that get returned by
        the API.
        """
        return Category.objects.all()

class LocationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Represents a specific location that a Facility can be found.

    GET /api/locations/
    Return all Location objects.

    Built-in query parameters:

    GET /api/locations/?search=
    Query parameter that returns objects that match a keyword provided in the search.

    GET /api/locations/?ordering=
    Query parameter that orders the returned objects based on the provided field to order by.

    Additionally, you can query against any field you like:

    ie.
    GET /api/locations/?building=Johnson+Center
    will return all Location objects located in the "Johnson Center" building.
    """
    # All model fields that are available for filtering
    FILTER_FIELDS = (
        # Location fields
        'building',
        'address',
        'on_campus'
    )

    # Associate a serializer with the ViewSet
    serializer_class = LocationSerializer

    # Setup filtering
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,
                       filters.OrderingFilter, )
    search_fields = FILTER_FIELDS
    ordering_fields = FILTER_FIELDS
    filter_fields = FILTER_FIELDS

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
    # All model fields that are available for filtering
    FILTER_FIELDS = (
        # Facility fields
        'facility_name',
        'tapingo_url',
        'facility_product_tags__name',
        # Category fields
        'facility_category__name',
        # Location fields
        'facility_location__building',
        'facility_location__address',
        'facility_location__on_campus',
        # Schedule fields
        'main_schedule__name',
        'main_schedule__valid_start',
        'main_schedule__valid_end',
        'special_schedules__name',
        'special_schedules__valid_start',
        'special_schedules__valid_end',
    )

    # Associate a serializer with the ViewSet
    serializer_class = FacilitySerializer

    # Setup filtering
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,
                       filters.OrderingFilter, )
    search_fields = FILTER_FIELDS
    ordering_fields = FILTER_FIELDS
    filter_fields = FILTER_FIELDS

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

    GET /api/schedules/
    Return all Schedule objects that have not expired. (ie. end_date is before today)

    Built-in query parameters:

    GET /api/schedules/?search=
    Query parameter that returns objects that match a keyword provided in the search.

    GET /api/schedules/?ordering=
    Query parameter that orders the returned objects based on the provided field to order by.

    Additionally, you can query against any field you like:

    ie.
    GET /api/schedules/?name=southside_main
    will return the Schedule object that has "southside_main" as its name.
    """
    # All model fields that are available for filtering
    FILTER_FIELDS = (
        # Schedule fields
        'name',
        'valid_start',
        'valid_end',
    )

    # Associate a serializer with the ViewSet
    serializer_class = ScheduleSerializer

    # Setup filtering
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,
                       filters.OrderingFilter, )
    search_fields = FILTER_FIELDS
    ordering_fields = FILTER_FIELDS
    filter_fields = FILTER_FIELDS

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
    Represents a time period when a Facility is open.

    Monday = 0, Sunday = 6.

    These objects are returned within a larger Schedule object and thus are not
    an endpoint that is query-able, so just return everything when requested.
    """
    # Associate a serializer with the ViewSet
    serializer_class = OpenTimeSerializer

    def get_queryset(self):
        """
        Handle incoming GET requests and enumerate objects that get returned by
        the API.
        """
        return OpenTime.objects.all()
