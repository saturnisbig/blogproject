# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils.six import python_2_unicode_compatible
from django.conf import settings

from blog.models import Entry


@python_2_unicode_compatible
class Comment(models.Model):
    content = models.TextField(u'评论内容')
    c_time = models.DateTimeField(u'评论发表时间', auto_now_add=True)

    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               related_name='%(class)s_related',
                               verbose_name=u'评论人')
    parent = models.ForeignKey('self', related_name='%(class)s_child_comments',
                               verbose_name=u'父评论', blank=True, null=True)
    rep_to = models.ForeignKey('self', related_name='%(class)s_rep_comment',
                               verbose_name=u'回复', blank=True, null=True)

    class Meta:
        '''元类，用来继承'''
        abstract = True

    def __str__(self):
        return self.content[:20]


class PostComment(Comment):
    post = models.ForeignKey(Entry, verbose_name=u'所属文章',
                             related_name='post_comments')

    class Meta:
        verbose_name = u'文章评论'
        verbose_name_plural = verbose_name
        ordering = ['-c_time']
