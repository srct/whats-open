from django.conf.urls import patterns, url

urlpatterns = patterns('website.views',
    url(r'^(?:ajax|api)/schedule/', 'ajax_schedule_data', name='schedule_data'),
    url(r'^$', 'facility_grid', name='facility_grid'),
)
