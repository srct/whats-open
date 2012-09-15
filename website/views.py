from website.models import Restaurant, Schedule
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.conf import settings


def alpha_grid(request):
    restaurants = Restaurant.objects.all()
    # Restaurants in lists of 4 to easily create rows in template
    restRows = [restaurants[x:x + 4] for x in xrange(0, len(restaurants), 4)]
    return render_to_response('alpha.html', {'restRows': restRows,
            'restaurants': restaurants})
