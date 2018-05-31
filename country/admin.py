# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from country.models import Country, Organisation


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent', 'level')


@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'desc', 'link')
