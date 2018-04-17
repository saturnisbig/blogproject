# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

    class Meta(AbstractUser.Meta):
        db_table = 'auth_user'
