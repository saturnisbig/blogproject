#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from django.conf.urls import url

from box import views

app_name = 'box'
urlpatterns = [
    url(r'^$', views.index, name='index')
]
