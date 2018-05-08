#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from django import template

register = template.Library()


@register.inclusion_tag('users/tags/user_avatar.html')
def show_user_avatar(user):
    '''显示用户的头像'''
    return {'user': user}
