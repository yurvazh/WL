from django.db import models

from django.contrib.auth.models import Permission, User
from django.urls import reverse

class Present(models.Model):
    title = models.CharField(max_length=200)
    creator = models.IntegerField(default=0)
    reserved = models.BooleanField(default=False)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('index', args=[])
