from django.conf.urls import patterns, include, url
from management.views import *

urlpatterns = patterns('',
        url(r'^$', index, name='index'),
        url(r'^login/$', mylogin, name='mylogin'),
)
