"""
api/views.py

Rest Framework Class Views

Each ViewSet determines what data is returned when an API endpoint is hit. In
addition, we define filtering and documentation for each of these endpoints. 
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

    - Random closings
    - Modified schedules being in effect
    - Election reminder
    - Advertising for other SRCT projects

    Alerts last for a period of time until the information is no longer dank.

    ---

    ## Default behavior

    [GET /api/alerts/](/api/alerts/?format=json)

    Return all active Alert objects.

    ## Built-in query parameters

    ### **Search**

    [GET /api/alerts/?search=](/api/alerts/?search=&format=json)

    Query parameter that returns objects that match a keyword provided in the search.

    **Example Usage**

    [GET /api/alerts/?search=srct](/api/alerts/?search=srct&format=json)

    Return any Alert objects that have the string "srct" located in one of its fields.

    ### **Ordering**

    [GET /api/alerts/?ordering=](/api/alerts/?ordering=&format=json)

    Query parameter that orders the returned objects based on the provided field to order by.

    **Example Usage**

    [GET /api/alerts/?ordering=urgency_tag](/api/alerts/?ordering=urgency_tag&format=json)

    Return all Alert objects ordered by urgency_tag ascending.

    [GET /api/alerts/?ordering=-urgency_tag](/api/alerts/?ordering=-urgency_tag&format=json)

    Return all Alert objects ordered by urgency_tag descending.

    ### **Field filtering**

    You can query directly against any field.

    **Example Usage**

    [GET /api/alerts/?urgency_tag=major](/api/alerts/?urgency_tag=major&format=json)

    Return all Alert objects that are tagged as "major" urgency.

    ## Custom query parameters

    ### **all_alerts**

    [GET /api/alerts/?all_alerts](/api/alerts/?all_alerts&format=json)

    Return all Alert objects.
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
        # Define ?all_alerts
        all_alerts = self.request.query_params.get('all_alerts', None)

        # Return all Alert objects if requested
        if all_alerts is not None:
            return Alert.objects.all()
        # Default behavior
        else:
            # Enumerate all Alert objects that are active
            alertable = [
                alert.pk
                for alert in Alert.objects.all()
                if alert.is_active()
            ]
            # Return active Alerts
            return Alert.objects.filter(pk__in=alertable)

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A Category is a grouping of Facilities that serve a common/similar purpose.

    Examples:

    - Dining
    - Gyms
    - Study areas (Libraries, The Ridge, JC, etc)

    ---

    ## Default behavior

    [GET /api/categories/](/api/categories/)

    Return all Category objects.

    ## Built-in query parameters

    ### **Search**

    [GET /api/categories/?search=](/api/categories/?search=&format=json)

    Query parameter that returns objects that match a keyword provided in the search.

    **Example Usage**

    [GET /api/categories/?search=din](/api/categories/?search=din&format=json)

    Return all Category objects that have a field that matches the string "din".

    ### **Ordering**

    [GET /api/categories/?ordering=](/api/categories/?ordering=&format=json)

    Query parameter that orders the returned objects based on the provided field to order by.

    **Example Usage**

    [GET /api/categories/?ordering=name](/api/categories/?ordering=name&format=json)

    Return all Category objects filtered by name ascending.

    [GET /api/categories/?ordering=-name](/api/categories/?ordering=-name&format=json)

    Return all Category objects filtered by name descending.

    ### **Field filtering**

    You can query directly against any field.

    **Example Usage**

    [GET /api/categories/?name=dining](/api/categories/?name=dining&format=json)

    Return the Category object that is named "dining".
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

    ---

    ## Default behavior

    [GET /api/locations/](/api/locations/?format=json)

    Return all Location objects.

    ## Built-in query parameters

    ### **Search**

    [GET /api/locations/?search=](/api/locations/?search=&format=json)

    Query parameter that returns objects that match a keyword provided in the search.

    **Example Usage**

    [GET /api/locations/?search=johnson](/api/locations/?search=johnson&format=json)

    Return all Location objects that have a field that matches the "johnson" string.

    ### **Ordering**

    Order the returned objects based on the provided field.

    [GET /api/locations/?ordering=](/api/locations/?ordering=&format=json)

    **Example Usage**

    [GET /api/locations/?ordering=building](/api/locations/?ordering=building&format=json)

    Return all Location objects ordered by building name ascending.

    [GET /api/locations/?ordering=-building](/api/locations/?ordering=-building&format=json)

    Return all Location objects ordered by building name descending.

    ### **Field filtering**

    You can query directly against any field.

    **Example Usage**

    [GET /api/locations/?building=Johnson+Center](/api/locations/?building=Johnson+Center&format=json)

    Return all Location objects located in the "Johnson Center" building.
    """
    # All model fields that are available for filtering
    FILTER_FIELDS = (
        # Location fields
        'building',
        'friendly_building',
        'address',
        'on_campus',
        'campus_region'
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

    ---

    ## Default behavior

    [GET /api/facilities/](/api/facilities/?format=json)

    Return all Facility objects. Additionally, we filter out stale special_schedules to reduce client side calculations.

    ## Built-in query parameters

    ### **Search**

    [GET /api/facilities/?search=](/api/facilities/?search=&format=json)

    Query parameter that returns objects that match a keyword provided in the search.

    **Example Usage**

    [GET /api/facilities/?search=south](/api/facilities/?search=south&format=json)

    Return all Facility objects that have a field that matches the string "south".

    ### **Ordering**

    [GET /api/facilities/?ordering=](/api/facilities/?ordering=&format=json)

    Query parameter that orders the returned objects based on the provided field to order by.

    **Example Usage**

    [GET /api/facilities/?ordering=facility_name](/api/facilities/?ordering=facility_name&format=json)

    Return all Facility objects ordered by facility_name ascending.

    [GET /api/facilities/?ordering=-facility_name](/api/facilities/?ordering=-facility_name&format=json)

    Return all Facility objects ordered by facility_name descending.

    ### **Field filtering**

    You can query directly against any field.

    **Example Usage**

    [GET /api/facilities/?facility_name=Southside](/api/facilities/?facility_name=Southside&format=json)

    Return the Facility object that has "Southside" as its name.

    ## Custom query parameters

    ### **open_now**

    [GET /api/facilities/?open_now](/api/facilities/?open_now&format=json)

    Only return open Facility objects.

    ### **closed_now**

    [GET /api/facilities/?closed_now](/api/facilities/?closed_now&format=json)

    Only return closed Facility objects.
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
        'facility_location_friendly_building',
        'facility_location__address',
        'facility_location__on_campus',
        'facility_location__campus_region',
        # Schedule fields
        'main_schedule__name',
        'main_schedule__valid_start',
        'main_schedule__valid_end',
        'main_schedule__twenty_four_hours',
        'main_schedule__schedule_for_removal',
        'special_schedules__name',
        'special_schedules__valid_start',
        'special_schedules__valid_end',
        'special_schedules__twenty_four_hours',
        'special_schedules__schedule_for_removal'
    )

    # Associate a serializer with the ViewSet
    serializer_class = FacilitySerializer

    # Setup filtering
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,
                       filters.OrderingFilter, )
    search_fields = FILTER_FIELDS
    ordering_fields = FILTER_FIELDS
    filter_fields = FILTER_FIELDS
    lookup_field = 'slug'

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
            open_facilities = [
                facility.pk
                for facility in Facility.objects.all()
                if facility.is_open()
            ]
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

    ---

    ## Default behavior

    [GET /api/schedules/](/api/schedules/?format=json)

    Return all Schedule objects that have not expired. (ie. end_date is before today)

    ## Built-in query parameters

    ### **Search**

    [GET /api/schedules/?search=](/api/schedules/?search=&format=json)

    Query parameter that returns objects that match a keyword provided in the search.

    **Example Usage**

    [GET /api/schedules/?search=south](/api/schedules/?search=south&format=json)

    Return all Schedule objects that have a field matching the string "south".

    ### **Ordering**

    [GET /api/schedules/?ordering=](/api/schedules/?ordering=&format=json)

    Query parameter that orders the returned objects based on the provided field to order by.

    **Example Usage**

    [GET /api/schedules/?ordering=name](/api/schedules/?ordering=name&format=json)

    Return all Schedule objects ordered by name ascending.

    [GET /api/schedules/?ordering=-name](/api/schedules/?ordering=-name&format=json)

    [GET /api/schedules/?ordering=name](/api/schedules/?ordering=name&format=json)

    Return all Schedule objects ordered by name ascending.
    Return all Schedule objects ordered by name descending.

    ### **Field filtering**

    You can query directly against any field.

    **Example Usage**

    [GET /api/schedules/?name=southside_main](/api/schedules/?name=southside_main&format=json)

    Return the Schedule object that has "southside_main" as its name.
    """
    # All model fields that are available for filtering
    FILTER_FIELDS = (
        # Schedule fields
        'name',
        'valid_start',
        'valid_end',
        'twenty_four_hours',
        'schedule_for_removal'
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
        filter_old_schedules = [
            schedule.pk
            for schedule in Schedule.objects.all()
            # If the schedule ended before today
            if schedule.valid_end and schedule.valid_start
            if schedule.valid_end < datetime.datetime.now(schedule.valid_end.tzinfo)
        ]
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
