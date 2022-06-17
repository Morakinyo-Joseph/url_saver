from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


class User(AbstractUser):
    pass


class UrlModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url_name = models.CharField(max_length=5000)
    time_saved = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return self.user
