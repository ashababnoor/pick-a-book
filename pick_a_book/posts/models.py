import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin
from users.models import Profile
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    purchase_date = models.DateField()
    description = models.TextField()

    edition = models.PositiveIntegerField(blank=True, null=True, default=None)
    publisher = models.CharField(max_length=250, blank=True, null=True, default=None)

    def __str__(self):
        return "Title: " + self.title


class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    image = models.FileField(upload_to='images/')

    def __str__(self):
        return "Img for post -> Title: " + self.post.title


class SellPost(Post):
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return super().__str__()    



class PreferredBook(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    edition = models.PositiveIntegerField(blank=True, null=True, default=None)
    publisher = models.CharField(max_length=250, blank=True, null=True, default=None)
    

class ExchangePost(Post):
    prefered_books = models.ManyToManyField(PreferredBook, related_name='exchange_post')