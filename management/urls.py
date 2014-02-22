from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from .views import index

management_urls = patterns('',
    url(
      regex=r'^$',
      view=index,
      name="index"
    )
)
