# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from .models import Category, Country, Site


def index(request):
    cties = Country.objects.all()
    return render(request, 'country/index.html', context={'countries': cties})

def get_country(request, pk):
    cty = get_object_or_404(Country, pk=pk)
    sites = Site.objects.filter(country=cty)
    cats = Category.objects.all()
    return render(request, 'country/sites.html', context={'country': cty,
                                                          'categories': cats,
                                                          'sites': sites})
