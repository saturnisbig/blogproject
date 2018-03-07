#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from django.conf.urls import url

from blog import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>\d+)/$', views.detail, name='detail'),
]
