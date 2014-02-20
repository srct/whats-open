from django.conf.urls import patterns, url

from . import views

from rest_framework.routers import DefaultRouter

#router = DefaultRouter()


urlpatterns = patterns('whats_open_sites.views',
    url(r'^(?:ajax|api)/schedule/', 'ajax_schedule_data', name='schedule_data'),
    url(r'^$', 'facility_grid', name='facility_grid'),

    url(r'^facilities/$', FacilitiesListView.as_view(), name='faciliites-list'),
    url(r'^facilities/(?P<category>/$', ),
    url(r'^facilities/(?P<slug>/$', FacilitiesDetailView.as_view(), name='facilities-detail'),
    url(r'^facilities/(?P<on_campus>/$', ),


)

