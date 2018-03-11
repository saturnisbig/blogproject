#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from django.conf.urls import url

from blog import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',
        views.archives, name='archives'),
    url(r'^categories/(?P<pk>\d+)/$', views.category, name='category'),
]
