# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.six import python_2_unicode_compatible

from mptt.models import MPTTModel, TreeForeignKey


@python_2_unicode_compatible
class Country(MPTTModel):
    name = models.CharField('名称', max_length=100, unique=True)
    desc = models.TextField('网站简介', blank=True)
    link = models.URLField('网站地址', blank=True)
    c_time = models.DateTimeField(auto_now_add=True)

    parent = TreeForeignKey('self', verbose_name='上一级', null=True,
                            on_delete=models.CASCADE,
                            blank=True, related_name='children')

    class Meta:
        verbose_name = verbose_name_plural = '国家/组织'

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


# @python_2_unicode_compatible
# class Site(models.Model):
#     title = models.CharField('网站名称', max_length=150)
#     desc = models.TextField('网站简介', blank=True)
#     link = models.URLField('网站地址', blank=True)
#     c_time = models.DateTimeField(auto_now_add=True)

#     country = models.ForeignKey(Country, verbose_name='所属群', null=True,
#                                 blank=True)

#     class Meta:
#         ordering = ('-c_time',)

#     def __str__(self):
#         return self.title
