from website.models import Restaurant
from django.shortcuts import render_to_response
import re


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
            'restaurants': restaurants})
