from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Post (models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField(blank = True)
    created_at = models.DateTimeField(auto_now_add = True)
    modified_at = models.DateTimeField(auto_now = True)

