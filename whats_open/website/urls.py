from django.conf.urls import patterns, include, url
from website.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'facilities', FacilityViewSet)
router.register(r'schedules', ScheduleViewSet)
router.register(r'opentimes', OpenTimeViewSet)

urlpatterns = patterns('website.views',
    url(r'^api/', include(router.urls)),
    url(r'^$', 'facility_grid', name='facility_grid'),
)
