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
    likes = models.IntegerField(default=0)
    published = models.BooleanField(default = False)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.music.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)
    
    def like(self):
        self.likes += 1 

    def publish(self):
        self.published = True

