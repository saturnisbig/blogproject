# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Country, Organisation


def index(request):
    nodes = Country.objects.all()
    # nodes = Country.objects.filter(level=0)
    return render(request, 'country/index.html', context={'nodes': nodes})


def get_country(request, pk):
    parent = Country.objects.get(id=int(pk))
    nodes = Country.objects.filter(parent=parent)
    # nodes = root.get_descendants()
    return render(request, 'country/index.html', {'parent': parent,
                                                  'nodes': nodes})


def get_organisation(request, pk):
    country = Country.objects.get(id=int(pk))
    root = Country.objects.root_node(tree_id=country.tree_id)
    orgs = country.organisation_set.all()
    return render(request, 'country/organisation.html', {'country': country,
                                                         'nodes': orgs,
                                                         'root': root})
