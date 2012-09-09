from website.models import Restaurant, Schedule
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.conf import settings

def alpha (request):
    restaurants = Restaurant.objects.all()
    #pass to django template
    return render_to_response('alpha.html', {'restaurants':restaurants})
