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
    archive_list = Entry.objects.dates('c_time', 'month', order='DESC')
    result = []
    if archive_list:
        for date in archive_list:
            date_list = Entry.objects.filter(c_time__year=date.year,
                                             c_time__month=date.month)
            result.append((date, len(date_list)))
    return result


@register.simple_tag
def get_categories():
    return Category.objects.annotate(num_posts=Count('entry')).filter(num_posts__gt=0)


@register.simple_tag
def get_tags():
    return Tag.objects.annotate(num_posts=Count('entry')).filter(num_posts__gt=0)

@register.simple_tag
def get_previous_post(post):
    return Entry.objects.filter(pk__lt=post.pk).order_by('-c_time').first()


@register.simple_tag
def get_next_post(post):
    return Entry.objects.filter(pk__gt=post.pk).order_by('c_time').first()
