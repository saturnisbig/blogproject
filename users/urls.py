#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from django.conf.urls import url

from users import views

app_name = 'users'
urlpatterns = [
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/change/$', views.change_profile, name='change_profile'),
]
