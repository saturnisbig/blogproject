# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=200)
    c_time = models.DateTimeField(auto_now_add=True)
    m_time = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=150)
    c_time = models.DateTimeField(auto_now_add=True)
    m_time = models.DateTimeField(auto_now=True)


class Entry(models.Model):
    title = models.CharField(max_length=200)
    # 文章简介，可以为空
    excerpt = models.CharField(max_length=255, blank=True)
    body = models.TextField()
    views = models.IntegerField(default=0)
    c_time = models.DateTimeField(auto_now_add=True)
    m_time = models.DateTimeField(auto_now=True)
    # 外键
    category = models.ForeignKey(Category)
    author = models.ForeignKey(User)
    # 标签，多对多关系，博文可以有多个标签，标签也可以存在于多篇博文
    tags = models.ManyToManyField(Tag, blank=True)
