from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from management.views import *
management_urls = patterns('',
        url('r^$', index, name='index'),
)
