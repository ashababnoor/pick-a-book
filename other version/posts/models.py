import datetime

from django.db import models
from django.contrib.auth.models import User

class ExchangePost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    purchase_date = models.DateField()
    description = models.TextField()
    edition = models.PositiveIntegerField(blank=True, null=True, default=None)
    publisher = models.CharField(max_length=250, blank=True, null=True, default=None)
    prefered_books = models.TextField()
    setVisible=models.IntegerField(default=1)
    catagory=models.CharField(max_length=250,default='None')

    def __str__(self):
        return self.title + "| id: " + str(self.id)

class ExchangePostImage(models.Model):
    post = models.ForeignKey(ExchangePost, default=None, on_delete=models.CASCADE)
    image = models.FileField(upload_to='images/')

    def __str__(self):
        return "Img for post -> Title: " + self.post.title

class Offers(models.Model):
    offered=models.ForeignKey(ExchangePost,default=None, on_delete=models.CASCADE,related_name='offered')
    offeringFor=models.ForeignKey(ExchangePost,default=None, on_delete=models.CASCADE,related_name='offeringFor')
    offeredUser=models.ForeignKey(User, on_delete=models.CASCADE,related_name='offeredUser')#user who is offering
    offeringForUser=models.ForeignKey(User, on_delete=models.CASCADE,related_name='offeringForUser')#user who is receieving the offer
    offeredUserAddr=models.CharField(max_length=255)

class ExchangePostDeliveryInfo(models.Model):
    book1=models.ForeignKey(ExchangePost,on_delete=models.CASCADE,related_name='book1')
    book2=models.ForeignKey(ExchangePost,on_delete=models.CASCADE,related_name='book2')
    # book1title = models.CharField(max_length=250,default=None,null=True)
    # book1author = models.CharField(max_length=250,default=None, null=True)
    # book2title = models.CharField(max_length=250,default=None, null=True)
    # book2author = models.CharField(max_length=250,default=None, null=True)
    book1DeliveryAddress=models.CharField(max_length=255,default=None, null=True)
    book2DeliveryAddress=models.CharField(max_length=255,default=None, null=True)

