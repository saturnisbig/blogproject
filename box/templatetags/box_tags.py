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


@register.simple_tag(takes_context=True)
def display_pages(context):
    is_paginated = context['is_paginated']
    if not is_paginated:
        return ''
    paginator = context['paginator']
    page = context['page_obj']
    per_page = 2
    first = False
    last = False
    left = []
    right = []
    left_has_more = False
    right_has_more = False
    page_number = page.number
    total_pages = paginator.num_pages
    page_range = list(paginator.page_range)

    if page_number == 1:
        right = page_range[page_number:(page_number+per_page)]
        if right[-1] < total_pages - 1:
            right_has_more = True

        if right[-1] < total_pages:
            last = True
    elif page_number == total_pages:
        # index in page_range
        index = total_pages - 1
        left_start = index - per_page
        left = page_range[(left_start) if left_start > 0 else 0:index]
        if left[0] > 2:
            left_has_more = True

        if left[0] > 1:
            first = True
    else:
        index = page_number - 1
        left_start = index - per_page
        left = page_range[left_start if left_start > 0 else 0:index]
        right = page_range[page_number:page_number+per_page]
        if left[0] > 2:
            left_has_more = True

        if left[0] > 1:
            first = True

        if right[-1] < total_pages - 1:
            right_has_more = True

        if right[-1] < total_pages:
            last = True

    context.update({
        'first': first,
        'left': left,
        'left_has_more': left_has_more,
        'right': right,
        'right_has_more': right_has_more,
        'last': last,
    })
    # 不返回这个的话，模板中会显示None
    return ''
