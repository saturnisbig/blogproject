# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse

from blog.models import Entry


def index(request):
    post_list = Entry.objects.all().order_by('-c_time')
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def detail(request, pk):
    post = get_object_or_404(Entry, pk=pk)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)
