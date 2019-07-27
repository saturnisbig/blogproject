# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from country.models import Country, Category, Site


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    pass
