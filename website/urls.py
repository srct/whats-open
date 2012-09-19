from django.conf.urls import patterns, url

urlpatterns = patterns('website.views',
    url(r'^$', 'restaurant_grid', name='restaurant_grid'),
)
