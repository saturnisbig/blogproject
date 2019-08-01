# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig
from django.db.models.signals import post_migrate


def rebuild_tree(sender, **kwargs):
    from .models import Country
    Country.objects.rebuild()


class CountryConfig(AppConfig):
    name = 'country'

    def ready(self):
        post_migrate.connect(rebuild_tree, sender=self)
