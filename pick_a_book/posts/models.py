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
    edition = models.PositiveIntegerField(blank=True)
    publisher = models.CharField(max_length=250, blank=True)
    

class ExchangePost(Post):
    prefered_books = models.ManyToManyField(PreferredBook, related_name='exchange_post')