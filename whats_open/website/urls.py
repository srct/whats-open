from django.conf.urls import patterns, include, url
from website.views import *
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from whats_open.settings import local as settings_local

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'facilities', FacilityViewSet)
router.register(r'schedules', ScheduleViewSet)
router.register(r'opentimes', OpenTimeViewSet)

urlpatterns = patterns('website.views',
    url(r'^api/', include(router.urls)),
    url(r'^$', 'facility_grid', name='facility_grid'),
) + static(settings_local.STATIC_URL, document_root=settings_local.STATIC_ROOT)
