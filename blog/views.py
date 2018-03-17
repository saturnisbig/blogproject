# -*- coding: utf-8 -*-

import markdown

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
# from django.http import HttpResponse

from blog.models import Entry, Category
from comments.forms import CommentForm


class IndexView(ListView):
    model = Entry
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    paginate_by = 5


class CategoryView(IndexView):
    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=cate)


class ArchiveView(IndexView):
    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        return super(ArchiveView, self).get_queryset().filter(
            c_time__year=year,
            c_time__month=month)


class EntryDetailView(DetailView):
    model = Entry
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        response = super(EntryDetailView, self).get(request, *args, **kwargs)
        self.object.increase_views()
        return response

    def get_object(self, queryset=None):
        post = super(EntryDetailView, self).get_object(queryset=queryset)
        post.body = markdown.markdown(post.body,
                                      extensions=[
                                          'markdown.extensions.extra',
                                          'markdown.extensions.codehilite',
                                          'markdown.extensions.toc'])
        return post

    def get_context_data(self, **kwargs):
        context = super(EntryDetailView, self).get_context_data(**kwargs)
        form = CommentForm()
        comment_list = self.object.comment_set.all()
        context.update({
            'form': form,
            'comment_list': comment_list
        })
        return context


def index(request):
    post_list = Entry.objects.all()
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def detail(request, pk):
    post = get_object_or_404(Entry, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    post.increase_views()
    form = CommentForm()
    comment_list = post.comment_set.all()
    context = {'post': post,
               'comment_list': comment_list,
               'form': form}
    return render(request, 'blog/detail.html', context)


def archives(request, year, month):
    post_list = Entry.objects.filter(c_time__year=int(year),
                                     c_time__month=int(month))
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Entry.objects.filter(category=cate)
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)
