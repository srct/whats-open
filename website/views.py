from django.template import RequestContext
from website.models import Restaurant, OpenTime, BaseModel
from website.api import export_data
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.decorators.http import condition
import hashlib
import json


def restaurant_grid(request):
    """Display the restaurants in a grid. Main page."""
    if 'sort' in request.GET:
        if request.GET['sort'] == 'location':
            # Display the grid by location (instead of listing alphabetically)
            pass  # Not implemented yet
    return render_to_response('restaurant_grid.html', 
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

