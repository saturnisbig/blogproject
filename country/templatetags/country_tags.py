#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from django import template

from country.models import Site, Category

register = template.Library()


@register.simple_tag
def get_sites_of_cat(cat, sites):
    result = []
    for site in sites:
        if site.category == cat:
            result.append(site)
    return result
