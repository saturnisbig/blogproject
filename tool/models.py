# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.six import python_2_unicode_compatible


@python_2_unicode_compatible
class CardID(models.Model):
    number = models.CharField('身份证号', max_length=18)
    place = models.CharField('身份证属地', max_length=100)
    c_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-number']

    def __str__(self):
        return self.place
