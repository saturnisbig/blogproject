# -*- coding: utf-8 -*-

from django.contrib import admin

from blog.models import Entry, Category, Tag
from users.models import User


class EntryAdmin(admin.ModelAdmin):
    date_hierarchy = 'c_time'
    exclude = ('views',)
    # display blog list info
    list_display = ['id', 'title', 'category', 'author', 'c_time', 'm_time',
                    'show_entry_comment']
    list_display_links = ('title',)
    list_filter = ('category', 'c_time')
    list_per_page = 20
    # 查询优化，将外键先缓存
    list_select_related = ('author', 'category')
    filter_horizontal = ('tags',)

    def get_queryset(self, request):
        '''限制用户只能查看自己发表的文章'''
        qs = super(EntryAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)

    def show_entry_comment(self, obj):
        latest_com = obj.post_comments.first()
        if latest_com:
            return latest_com.content[:20]
        else:
            return ''
    show_entry_comment.short_description = '最新评论'

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'author':
            kwargs['queryset'] = User.objects.filter(is_staff=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'c_time', 'm_time', )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'c_time', 'm_time')


admin.site.register(Entry, EntryAdmin)
