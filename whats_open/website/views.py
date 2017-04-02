# Future Imports
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

# Python stdlib Imports
import hashlib
import json

# Django Imports
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.decorators.http import condition
from django.views.generic import ListView, DetailView
from model_utils.models import TimeStampedModel

# App Imports
from .models import Facility, OpenTime, Category, Schedule
from .api import export_data
from .serializers import  CategorySerializer, FacilitySerializer, ScheduleSerializer, OpenTimeSerializer

# Other Imports
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Rest Framework Class Views
class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class FacilityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer

    def get_queryset(self):
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
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

class OpenTimeViewSet(viewsets.ModelViewSet):
    queryset = OpenTime.objects.all()
    serializer_class = OpenTimeSerializer

def gen_etag(request):
    return hashlib.sha1(str(OpenTime.objects.all())).hexdigest()

def gen_last_modified(request):
    return TimeStampedModel.objects.all().order_by('-last_modified')[0].last_modified
