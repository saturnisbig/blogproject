# -*- coding: utf-8 -*-

from django.shortcuts import render
# from django.http import HttpResponse

from blog.models import Entry


def index(request):
    post_list = Entry.objects.all().order_by('-created_time')
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)
