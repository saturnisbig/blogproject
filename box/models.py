# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.six import python_2_unicode_compatible


@python_2_unicode_compatible
class Subject(models.Model):
    name = models.CharField('主题', max_length=200, default="其他")
    c_time = models.DateTimeField('创建时间', auto_now_add=True)
    m_time = models.DateTimeField('修改时间', auto_now=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Author(models.Model):
    name = models.CharField('姓名', max_length=100)
    birth_date = models.DateField('出生日期', blank=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Publisher(models.Model):
    name = models.CharField('出版社名称', max_length=300)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Book(models.Model):
    name = models.CharField('书名', max_length=250)
    authors = models.ManyToManyField(Author, verbose_name='作者')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE,
                                  verbose_name='出版社')
    pub_date = models.DateField('出版日期', blank=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Summary(models.Model):
    content = models.TextField('摘要内容')
    c_time = models.DateTimeField('创建时间', auto_now_add=True)
    m_time = models.DateTimeField('修改时间', auto_now=True)

    subjects = models.ManyToManyField(Subject, verbose_name='所属主题')
    book = models.ForeignKey(Book, verbose_name='所属书本')

    class Meta:
        verbose_name = '读书摘要'
        verbose_name_plural = verbose_name
        ordering = ['-c_time']

    def __str__(self):
        return self.content[:50]
