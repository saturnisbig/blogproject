#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from django.conf.urls import url

from box import views

urlpatterns = [
    url(r'^$', views.index, name='index')
]
