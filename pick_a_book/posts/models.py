import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin
from users.models import UserProfile


class Post(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    purchase_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return "User: " + self.user + " | Title: " + self.title


class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    image = models.FileField(upload_to='images/')

    def __str__(self):
        return "Img for post -> " + "User: " + self.post.user + " | Title: " + self.post.title


class SellPost(Post):
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return "Sell post ->" + super().__str__()