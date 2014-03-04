from django.conf.urls import patterns, include, url
from management.views import *

urlpatterns = patterns('',
        url('', index, name='index'),
)
