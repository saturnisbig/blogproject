# -*- coding: utf-8 -*-

import markdown

from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse

from blog.models import Entry, Category


def index(request):
    post_list = Entry.objects.all().order_by('-c_time')
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
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def archives(request, year, month):
    post_list = Entry.objects.filter(c_time__year=int(year),
                                     c_time__month=int(month))
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Entry.objects.filter(category=cate).order_by('-c_time')
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)
