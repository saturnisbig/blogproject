from django.contrib import admin

from blog.models import Entry, Category, Tag


class EntryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author', 'c_time', 'm_time']


admin.site.register(Entry, EntryAdmin)
admin.site.register(Category)
admin.site.register(Tag)
