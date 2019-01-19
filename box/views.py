# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from box.models import Summary, Subject, Book, Author


class BoxIndexView(ListView):
    model = Summary
    template_name = 'box/index.html'
    context_object_name = 'summaries'
    paginate_by = 5


class BookListView(ListView):
    model = Book
    template_name = 'box/book_list.html'
    context_object_name = 'books'
    paginate_by = 10


class BookDetailView(DetailView):
    model = Book
    template_name = 'box/book_detail.html'
    context_object_name = 'book'
    pk_url_kwarg = 'book_id'

    # def get_context_data(self, **kwargs):
    #     context = super(BookDetailView, self).get_context_data(**kwargs)
    #     book = context['book']
    #     return context

class SubjectListView(ListView):
    model = Subject
    template_name = 'box/subject_list.html'
    context_object_name = 'subjects'
    is_paginated = 10


class SubjectDetailView(DetailView):
    model = Subject
    template_name = 'box/subject_detail.html'
    context_object_name = 'subject'
    pk_url_kwarg = 'subject_id'


class SummaryDetailView(DetailView):
    model = Summary
    template_name = 'box/summary_detail.html'
    context_object_name = 'summary'

class AuthorBooksView(BookListView):
    def get_context_data(self, **kwargs):
        context = super(AuthorBooksView, self).get_context_data(**kwargs)
        author = get_object_or_404(Author, pk=self.kwargs.get('author_id'))
        context['current_obj'] = author
        return context

    def get_queryset(self):
        author = get_object_or_404(Author, pk=self.kwargs.get('author_id'))
        return super(AuthorBooksView, self).get_queryset().filter(authors=author)
