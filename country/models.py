# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.six import python_2_unicode_compatible

# from mptt.models import MPTTModel, TreeForeignKey


@python_2_unicode_compatible
class Country(models.Model):
    name = models.CharField('名称', max_length=100, unique=True)
    c_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = verbose_name_plural = '国家'

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField('名称', max_length=150, unique=True)
    c_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = verbose_name_plural = '类别'

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Site(models.Model):
    title = models.CharField('网站名称', max_length=150)
    link = models.URLField('网站地址', blank=True)
    desc = models.TextField('网站简介', blank=True)
    c_time = models.DateTimeField(auto_now_add=True)

    country = models.ForeignKey(Country, verbose_name='所属国家', null=True,
                                blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, verbose_name='所属类别', null=True,
                                 blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = verbose_name_plural = '网站信息'
        ordering = ('-c_time',)

    def __str__(self):
        return self.title
