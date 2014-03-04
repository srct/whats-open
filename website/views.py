from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.decorators.http import condition
from django.views.generic import ListView, DetailView

from .models import Facility, OpenTime, Category, Schedule 
from .api import export_data
from .serializers import  CategorySerializer, FacilitySerializer, ScheduleSerializer, OpenTimeSerializer

from rest_framework import viewsets 
from rest_framework.response import Response

import hashlib
import json


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

class OpenTimeViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = OpenTimeSerializer

class FacilityListView(ListView):
    model = Facility
    queryset = Facility.objects.all()

class FacilityViewSet(viewsets.ViewSet):
    def list(self,request):
        queryset = Facility.objects.all()
        serializer = FacilitySerializer(queryset,many=True)
        return Response(serializer.data)

class FacilityCategoryListView(ListView):
    model = Facility
    def get_queryset(self):
        return Facility.objects.filter(category=self.kwargs['category'])

class FacilityCategoryListViewSet(viewsets.ViewSet):
    def list(self,request):
        queryset = Facility.objects.filter(category=self.kwargs['category'])
        serializer = FacilitySerializer(queryset,many=True)
        return Response(serializer.data)

class FacilityStatusListView(ListView):
    model = Facility
    def get_queryset(self):
        return Facility.objects.filter(on_campus=self.kwargs['on_campus'])
    
class FacilityStatusListViewSet(viewsets.ViewSet):
    def list(self,request):
        queryset = Facility.objects.filter(on_campus=self.kwargs['on_campus'])
        serializer = FacilitySerializer(queryset,many=True)
        return Response(serializer.data)

class FacilityDetailView(DetailView):
    model = Facility

class FacilityDetailViewSet(viewsets.ViewSet):
    def retreive(self,request,slug=None):
        queryset = Facility.obejcts.all()
        facility = get_object_or_404(queryset,slug=slug)
        serializer = FacilitySerializer(facility)
        return Response(serializer.data)

class ScheduleDetailView(DetailView):
    model = Schedule
    def retreive(self,request,pk=None):
        queryset = Schedule.objects.all()
        schedule = get_object_or_404(queryset,pk=pk)
        serializer = ScheduleSerializer(schedule)
        return Response(serializer.data)

class OpenTimeDetailView(DetailView):
    model = OpenTime
    def retrieve(self,request,pk=None):
        queryset = OpenTime.objects.all()
        open_time = get_object_or_404(queryset,pk=pk)
        serializer = OpenTimeSerializer(open_time)
        return Response(serializer.data)
"""
class CategoryListView(ListView):
    model = Categories
"""


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
    return BaseModel.objects.all().order_by('-last_modified')[0].last_modified


@condition(etag_func=gen_etag, last_modified_func=gen_last_modified)
def ajax_schedule_data(request):
    # Wrapping up in an object to avoid possible CSRF attack on top-level
    # arrays in JSON objects
    return HttpResponse(json.dumps({'data': export_data()}, indent=4),
            content_type="application/json")

