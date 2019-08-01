# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from mptt.admin import MPTTModelAdmin

from country.models import Country, Category, Site


@admin.register(Country)
class CountryMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ['title', 'link', 'category', 'country', 'c_time']
    list_filter = ('category', 'country')
    list_per_page = 20
