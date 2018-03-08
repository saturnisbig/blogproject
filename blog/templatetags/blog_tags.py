#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from django import template

from blog.models import Entry, Category

register = template.Library()


@register.simple_tag
def get_recent_posts(num=5):
    return Entry.objects.all().order_by('-c_time')[:num]


@register.simple_tag
def archive():
    return Entry.objects.dates('c_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    return Category.objects.all()
