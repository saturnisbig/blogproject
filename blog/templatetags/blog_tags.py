#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from django import template
from django.db.models.aggregates import Count

from blog.models import Entry, Category, Tag

register = template.Library()


@register.simple_tag
def get_recent_posts(num=5):
    return Entry.objects.all().order_by('-c_time')[:num]


@register.simple_tag
def archive():
    return Entry.objects.dates('c_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    return Category.objects.annotate(num_posts=Count('entry')).filter(num_posts__gt=0)


@register.simple_tag
def get_tags():
    return Tag.objects.annotate(num_posts=Count('entry')).filter(num_posts__gt=0)
