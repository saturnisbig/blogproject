# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from country.models import Country


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'desc', 'link', 'parent', 'level')
