from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from .helpers import *
from django.urls import reverse



class BlogModel(models.Model):
    title = models.CharField(max_length=1000)
    content = FroalaField()
    slug = models.SlugField(max_length=1000 , null=True , blank=True)
    user = models.ForeignKey(User, blank=True , null=True , on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog')
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def save(self , *args, **kwargs): 
        self.slug = generate_slug(self.title)
        super(BlogModel, self).save(*args, **kwargs)
        
    # def get_absolute_url(self):
	#     return reverse('blog_detail', kwargs={'pk':self.pk})
    
    
class Comment(models.Model):
    # blog_id = models.ForeignKey(BlogModel,on_delete=models.CASCADE,related_name='comments')
    blog_id = models.SlugField(max_length=1000 , null=True , blank=True)
    name = models.CharField(max_length=80)
    # email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    # active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
    
    


