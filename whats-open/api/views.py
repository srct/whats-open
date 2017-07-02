"""
api/views.py

Rest Framework Class Views
"""
# Future Imports
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

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
        return Alert.objects.all()

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Return all Category objects.
    """
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()

class LocationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Return all Location objects.
    """
    serializer_class = LocationSerializer

    def get_queryset(self):
        return Location.objects.all()

class FacilityViewSet(viewsets.ReadOnlyModelViewSet):
    """
    """
    serializer_class = FacilitySerializer

    def get_queryset(self):
        """
        """
        open_now = self.request.query_params.get('open_now', None)
        if open_now is not None:
            results = []
            for fac in Facility.objects.all():
                if fac.is_open():
                    results.append(fac.pk)
            return Facility.objects.filter(pk__in=results)
        else:
            return Facility.objects.all()

class ScheduleViewSet(viewsets.ModelViewSet):
    """
    Return all Schedule objects.
    """
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        return Schedule.objects.all()

class OpenTimeViewSet(viewsets.ModelViewSet):
    """
    Return all OpenTime objects.
    """
    serializer_class = OpenTimeSerializer

    def get_queryset(self):
        return OpenTime.objects.all()