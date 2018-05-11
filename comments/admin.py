from django.contrib import admin

from .models import PostComment


@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    exclude = ('rep_to', 'parent', 'c_time')
    list_display = ('id', 'author', 'post', 'content', 'c_time')
    list_display_links = ('content',)
