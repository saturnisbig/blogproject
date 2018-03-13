# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import markdown

from django.shortcuts import reverse
from django.db import models
from django.contrib.auth.models import User
from django.utils.six import python_2_unicode_compatible
from django.utils.html import strip_tags


@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=200)
    c_time = models.DateTimeField(auto_now_add=True)
    m_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=150)
    c_time = models.DateTimeField(auto_now_add=True)
    m_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Entry(models.Model):
    title = models.CharField(max_length=200)
    # 文章简介，可以为空
    excerpt = models.CharField(max_length=255, blank=True)
    body = models.TextField()
    views = models.PositiveIntegerField(default=0)
    c_time = models.DateTimeField(auto_now_add=True)
    m_time = models.DateTimeField(auto_now=True)
    # 外键
    category = models.ForeignKey(Category)
    author = models.ForeignKey(User)
    # 标签，多对多关系，博文可以有多个标签，标签也可以存在于多篇博文
    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        ordering = ['-c_time']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.excerpt:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            self.excerpt = strip_tags(md.convert(self.body))[:54]

        super(Entry, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])
