#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from django.conf.urls import url

from box import views

app_name = 'box'
urlpatterns = [
    url(r'^$', views.BoxIndexView.as_view(), name='index'),
    url(r'^books/$', views.BookListView.as_view(), name='book_list'),
    url(r'^book/(?P<book_id>\d+)/$', views.BookDetailView.as_view(),
        name='book_detail'),
    url(r'^subjects/$', views.SubjectListView.as_view(), name='subject_list'),
    url(r'^subject/(?P<subject_id>\d+)/$', views.SubjectDetailView.as_view(),
        name='subject_detail'),
    url(r'^author/(?P<author_id>\d+)/$', views.AuthorBooksView.as_view(),
        name='author_books'),
    url(r'^summary/(?P<pk>\d+)/$', views.SummaryDetailView.as_view(),
        name='summary_detail'),
]
