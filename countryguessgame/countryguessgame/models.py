from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    score = models.IntegerField(default=0)
    last_played = models.DateTimeField(auto_now=True)

class GameRecord(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    country = models.CharField(max_length=100)
    correct = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)