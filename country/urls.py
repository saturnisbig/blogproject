#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from django.conf.urls import url

from country import views

app_name = 'country'
urlpatterns = [
    url(r'^$', views.index, name='index'),
]
