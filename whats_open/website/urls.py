from django.conf.urls import patterns, include, url
from website.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'facilities', FacilityViewSet)
router.register(r'schedules', ScheduleViewSet)
router.register(r'opentimes', OpenTimeViewSet)

urlpatterns = patterns('website.views',
    #url(r'^(?:ajax|api)/schedule/', 'ajax_schedule_data', name='schedule_data'),

    url(r'^api/', include(router.urls)),
    url(r'^$', 'facility_grid', name='facility_grid'),
    #facilities open urls
    #url(r'^facilities/$', FacilityListView.as_view(), name='faciliites-list'),
    #url(r'^facilities/(?P<category>)/$', FacilityCategoryListView.as_view(), name='facilities-list-by-cat'),
    #url(r'^facilities/(?P<slug>)/$', FacilityDetailView.as_view(), name='facilities-detail'),
    #url(r'^facilities/(?P<on_campus>)/$', FacilityStatusListView.as_view(), name='facilities-list-by-status'),

    #schedules urls
    #url(r'^schedule/(?P<pk>)/$', ScheduleDetailView.as_view(), name='schedule-detail'),

    #opentime urls
    #url(r'^open-time/(?P<pk>)/$', OpenTimeDetailView.as_view(), name='open-time-detail'),
)
