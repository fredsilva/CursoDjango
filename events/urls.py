# encoding: utf-8

from django.conf.urls import patterns, include, url

urlpatterns = patterns('events.views',
    url(r'^$', 'index', name='events'),
    url(r'^(\d+)/$', 'details', name='events_details')
)