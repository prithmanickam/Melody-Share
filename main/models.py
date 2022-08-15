from django.db import models

from django.contrib.auth.models import User
from django.db.models.fields import related
from django.urls import reverse
from datetime import datetime, date


class Song(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=100)
    music = models.FileField(upload_to='music/songs/')
    cover = models.ImageField(upload_to='music/covers/', null=True, blank=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.music.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)
