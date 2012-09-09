from website.models import Restaurant, Schedule
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.conf import settings

def alpha (request):
    restaurants = Restaurant.objects.all()
    #pass to django template
    restRows = [restaurants[x:x+4] for x in xrange(0, len(restaurants), 4)]
    return render_to_response('alpha.html', {'restaurants':restRows})
