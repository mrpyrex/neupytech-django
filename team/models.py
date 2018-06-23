from django.db import models
from django.utils import timezone

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    bio = models.TextField()
    pic = models.ImageField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name