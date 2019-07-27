#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from django.conf.urls import url

from country import views

app_name = 'country'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>\d+)/$', views.get_country, name='get_country'),
    # url(r'^organisation/(?P<pk>\d+)/$', views.get_organisation,
    #     name='get_organisation'),
]
