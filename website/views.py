from django.template import RequestContext
from website.models import Restaurant, OpenTime, BaseModel, export_data
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.decorators.http import condition
import re
import hashlib
import json


def restaurant_grid(request):
    """Display the restaurants in a grid. Main page."""
    if 'sort' in request.GET:
        if request.GET['sort'] == 'location':
            # Display the grid by location (instead of listing alphabetically)
            pass  # Not implemented yet
    restaurants = Restaurant.objects.all()
    # Sort the restaurants by alphabetical order ignoring "the" and "a"
    restaurants = sorted(restaurants,
            key=lambda r: re.sub('^(the|a) ', '', r.name, count=1,
            flags=re.IGNORECASE))
    # Restaurants in lists of 4 to easily create rows in template
    restRows = [restaurants[x:x + 4] for x in xrange(0, len(restaurants), 4)]
    return render_to_response('restaurant_grid.html', {'restRows': restRows,
            'restaurants': restaurants},
            context_instance=RequestContext(request))

def gen_etag(request):
    return hashlib.sha1(str(OpenTime.objects.all())).hexdigest()

def gen_last_modified(request):
    return BaseModel.objects.all().order_by('-last_modified')[0].last_modified


@condition(etag_func=gen_etag, last_modified_func=gen_last_modified)
def ajax_schedule_data(request):
    # Wrapping up in an object to avoid possible CSRF attack on top-level
    # arrays in JSON objects
    return HttpResponse(json.dumps({'data': export_data()}),
            content_type="application/json")

