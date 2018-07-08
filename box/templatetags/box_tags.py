#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from django import template
from django.db.models.aggregates import Count

from box.models import Subject, Book

register = template.Library()


@register.simple_tag
def get_recent_books(num=5):
    return Book.objects.all()[:num]


@register.simple_tag
def get_recent_subjects(num=5):
    return Subject.objects.all()[:num]
