"""
Rest Framework Class Views
"""
# Future Imports
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

# App Imports
from .models import Facility, OpenTime, Category, Schedule, Location
from .serializers import (CategorySerializer, FacilitySerializer,
                          ScheduleSerializer, OpenTimeSerializer, 
                          LocationSerializer)

# Other Imports
from rest_framework import viewsets

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class LocationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class FacilityViewSet(viewsets.ReadOnlyModelViewSet):
    """
    """
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer

    def get_queryset(self):
        """
        """
        queryset = Facility.objects.all()
        open_now = self.request.query_params.get('open', None)
        if open_now is not None:
            results = []
            for fac in queryset:
                if fac.isOpen():
                    results.append(fac)
            return results
        else:
            return queryset

class ScheduleViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

class OpenTimeViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = OpenTime.objects.all()
    serializer_class = OpenTimeSerializer
