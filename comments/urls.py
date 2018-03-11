#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from django.conf.urls import url

from comments import views

app_name = 'comments'
urlpatterns = [
    url(r'^comments/post/(?P<post_pk>\d+)/$', views.post_comment,
        name='post_comment'),
]

