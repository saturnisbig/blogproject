# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, DetailView

from box.models import Summary, Subject, Book


class BoxIndexView(ListView):
    model = Summary
    template_name = 'box/index.html'
    context_object_name = 'summaries'
    paginate_by = 5


class BookDetailView(DetailView):
    model = Book
    template_name = 'box/book_detail.html'
    context_object_name = 'book'
    pk_url_kwarg = 'book_id'

    # def get_context_data(self, **kwargs):
    #     context = super(BookDetailView, self).get_context_data(**kwargs)
    #     book = context['book']
    #     return context


class SubjectDetailView(DetailView):
    model = Subject
    template_name = 'box/subject_detail.html'
    context_object_name = 'subject'
    pk_url_kwarg = 'subject_id'


class SummaryDetailView(DetailView):
    model = Summary
    template_name = 'box/summary_detail.html'
    context_object_name = 'summary'
