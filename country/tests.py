# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from .models import Country, Category, Site


class SiteModelTests(TestCase):

    def test_site_must_have_country(self):
        # s = Site.objects.create(title='日本新闻网')
        pass

