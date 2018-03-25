#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from django.contrib.syndication.views import Feed

from blog.models import Entry


class EntryRSSFeed(Feed):
    title = 'Teddy and Pudding'
    link = '/blog/'
    description = '网站博文情况'

    def items(self):
        return Entry.objects.all()

    def item_title(self, item):
        return u'[%s] %s' % (item.category, item.title)

    def item_description(self, item):
        return item.body
