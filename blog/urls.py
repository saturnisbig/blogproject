#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from django.conf.urls import url

from blog import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^post/(?P<pk>\d+)/$', views.EntryDetailView.as_view(), name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',
        views.ArchiveView.as_view(), name='archives'),
    url(r'^archives/$', views.archives_list, name='archives_list'),
    url(r'^categories/(?P<slug>[\w-]+)/$', views.CategoryView.as_view(),
        name='category'),
    url(r'^tag/(?P<pk>\d+)/$', views.TagView.as_view(), name='tag'),
    url(r'^popular/$', views.PopularView.as_view(), name='popular'),
]
