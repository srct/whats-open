# Future Imports
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

# App Imports
from .models import Facility, OpenTime, Category, Schedule
from .serializers import (CategorySerializer, FacilitySerializer,
                          ScheduleSerializer, OpenTimeSerializer)

# Other Imports
from rest_framework import viewsets

# Rest Framework Class Views
class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

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
                print(fac)
                if fac.isOpen():
                    print(True)
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
