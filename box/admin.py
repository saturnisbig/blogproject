# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from box.models import Book, Author, Publisher, Summary, Subject

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(Summary)
class SummaryAdmin(admin.ModelAdmin):
    list_display = ('content', 'book', 'c_time')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass
