# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    site_url = models.URLField('个人网址', blank=True, help_text='网址必须以http开头的完整形式')
    avatar = models.ImageField(upload_to='avatar',
                               default='avatar/default.png',
                               verbose_name='头像')

    class Meta(AbstractUser.Meta):
        db_table = 'auth_user'

    def __str__(self):
        return self.username
