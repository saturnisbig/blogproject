# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Country


def index(request):
    nodes = Country.objects.filter(name__isnull=False)
    # nodes = Country.objects.filter(level=0)
    return render(request, 'country/index.html', context={'nodes': nodes})
