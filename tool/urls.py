#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from django.conf.urls import url

from tool import views

app_name = 'tool'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^webcolor/$', views.webcolor, name='webcolor'),
    url(r'^convert_color/$', views.convert_color, name='convert_color'),
    url(r'^idplace/$', views.id_place, name='id_place'),
    url(r'^getcardid/$', views.get_cardid, name='get_cardid'),
    url(r'^getcardname/$', views.get_cardname, name='get_cardname'),
]
