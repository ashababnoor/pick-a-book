from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Library(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=255)
    longitude=models.FloatField()
    latitude=models.FloatField()

    def __str__(self):
        return "Title: " + self.name

