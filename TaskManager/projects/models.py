from django.db import models
from django.utils import timezone
from django.contrib.auth.admin import User


class Project(models.Model):
    class Status(models.TextChoices):
        FINISHED = 'finished'
        DURING = 'during'
        STARTED = 'started'

    objects = models.Manager()
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects_project')
    description = models.TextField()
    technology = models.CharField(max_length=100)
    created = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.STARTED)
    # image = models.FilePathField(default="")
    image = models.ImageField(upload_to='img')
