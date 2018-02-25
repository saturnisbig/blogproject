# -*- coding: utf-8 -*-

from django.shortcuts import render
# from django.http import HttpResponse


def index(request):
    context = {'title': '我的博客首页',
               'content': '欢迎访问我的博客首页'}
    return render(request, 'blog/index.html', context)
