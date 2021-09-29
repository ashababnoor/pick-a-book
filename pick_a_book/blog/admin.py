from django.contrib import admin

# Register your models here.

from .models import BlogModel, Comment

admin.site.register(BlogModel)
admin.site.register(Comment)