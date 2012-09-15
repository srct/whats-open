from django.conf.urls import patterns, include, url

urlpatterns = patterns('website.views',
    url(r'^$', 'alpha_grid', name = 'alpha_grid'),
)


