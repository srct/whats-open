from django.conf.urls import patterns, include, url
from django.contrib.sites.models import Site
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^', include('website.urls')),
    url(r'management/', include('management.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login', {
        'template_name': 'login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {
        'next_page': '/'}),

)
