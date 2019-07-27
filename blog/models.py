# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import markdown

from django.shortcuts import reverse
from django.db import models
# from django.contrib.auth.models import User
from django.utils.six import python_2_unicode_compatible
from django.utils.html import strip_tags
from django.conf import settings


@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField('类别名称', max_length=200)
    slug = models.SlugField(blank=True, max_length=50)
    c_time = models.DateTimeField('创建时间', auto_now_add=True)
    m_time = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        verbose_name = verbose_name_plural = '分类'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:category', kwargs={'pk': self.pk})


@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField('标签', max_length=150)
    slug = models.SlugField(blank=True, max_length=50)
    c_time = models.DateTimeField('创建时间', auto_now_add=True)
    m_time = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        verbose_name = verbose_name_plural = '标签'

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Entry(models.Model):
    title = models.CharField('文章标题', max_length=200)
    slug = models.SlugField(blank=True, max_length=100)
    # 文章简介，可以为空
    excerpt = models.CharField('摘要', max_length=255, blank=True,
                               help_text='不填写则自动生成')
    body = models.TextField('文章内容')
    views = models.PositiveIntegerField('阅读量', default=0)
    c_time = models.DateTimeField('创建时间', auto_now_add=True)
    m_time = models.DateTimeField('修改时间', auto_now=True)
    # 外键
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 verbose_name='类别')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='作者',
                               on_delete=models.CASCADE)
    # 标签，多对多关系，博文可以有多个标签，标签也可以存在于多篇博文
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='标签')

    class Meta:
        ordering = ['-c_time']
        verbose_name = verbose_name_plural = '博文'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.excerpt:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            self.excerpt = strip_tags(md.convert(self.body))[:54]

        super(Entry, self).save(*args, **kwargs)

    def get_absolute_url(self):
        # dt = {'slug': self.slug} if self.slug else {'pk': self.pk}
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])
