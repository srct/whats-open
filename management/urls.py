from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

management_urls = patterns('management.views',
        url('r^/', 'index', name='index'),
)
