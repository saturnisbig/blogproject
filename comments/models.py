from __future__ import unicode_literals

from django.db import models
from django.utils.six import python_2_unicode_compatible

from blog.models import Entry


@python_2_unicode_compatible
class Comment(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    url = models.URLField(blank=True)
    content = models.TextField()
    c_time = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey(Entry)

    def __str__(self):
        return self.content[:20]
