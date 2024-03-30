from django.db import models
from django.utils import timezone
# Create your models here.


class ChatHistory(models.Model):
    username = models.CharField(max_length=200)
    user = models.CharField(max_length=200)
    message = models.TextField()
    datetime = models.DateTimeField(default=timezone.now)


class ChatHistoryBackup(models.Model):
    username = models.CharField(max_length=200)
    user = models.CharField(max_length=200)
    message = models.TextField()
    datetime = models.DateTimeField(default=timezone.now)


class Prompt(models.Model):
    username = models.CharField(max_length=200)
    user = models.CharField(max_length=200)
    message = models.TextField()
    datetime = models.DateTimeField(default=timezone.now)
