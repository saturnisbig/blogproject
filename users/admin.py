# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class OuserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active', 'date_joined')
    # fieldsets = (
    #     ('基础信息', {'fields': (('username', 'email'))})
    # )
    filter_horizontal = ('groups', 'user_permissions',)
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
