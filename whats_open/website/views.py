from django.template import RequestContext
from website.models import Facility, OpenTime
from website.api import export_data
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.decorators.http import condition
from django.views.generic import ListView, DetailView
from model_utils.models import TimeStampedModel

from website.models import Facility, OpenTime, Category, Schedule
from website.api import export_data
from website.serializers import  CategorySerializer, FacilitySerializer, ScheduleSerializer, OpenTimeSerializer

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

import hashlib
import json

# Rest Framework Class Views
class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class FacilityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer

    def get_queryset(self):
        queryset = Facility.objects.all()
        open_now = self.request.QUERY_PARAMS.get('open', None)
        if open_now is not None:
            results = []
            for fac in queryset:
                print fac
                if fac.isOpen():
                    print True
                    results.append(fac)
            return results
        else:
            return queryset

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

class OpenTimeViewSet(viewsets.ModelViewSet):
    queryset = OpenTime.objects.all()
    serializer_class = OpenTimeSerializer

def facility_grid(request):
    """Display the facilities in a grid. Main page."""
    if 'sort' in request.GET:
        if request.GET['sort'] == 'location':
            # Display the grid by location (instead of listing alphabetically)
            pass  # Not implemented yet
    return render_to_response('facility_grid.html',
            context_instance=RequestContext(request))

def gen_etag(request):
    return hashlib.sha1(str(OpenTime.objects.all())).hexdigest()

def gen_last_modified(request):
    return TimeStampedModel.objects.all().order_by('-last_modified')[0].last_modified


@condition(etag_func=gen_etag, last_modified_func=gen_last_modified)
def ajax_schedule_data(request):
    # Wrapping up in an object to avoid possible CSRF attack on top-level
    # arrays in JSON objects
    return HttpResponse(json.dumps({'data': export_data()}, indent=4),
            content_type="application/json")
