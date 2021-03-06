from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField(blank = True)
    tags = models.CharField(max_length = 200)
    created_at = models.DateTimeField(auto_now_add = True)
    modified_at = models.DateTimeField(auto_now = True)
    username = models.CharField(max_length = 100)

    def text_edit(self):
        return str(self.pk) + '/edit/'

    def text_delete(self):
        return str(self.pk) + '/delete/'

