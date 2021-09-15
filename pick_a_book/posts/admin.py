from django.contrib import admin
from django.db import models
from .models import SellPost, PostImage

class PostImageAdmin(admin.StackedInline):
    model = PostImage

@admin.register(SellPost)
class SellPostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    fieldsets = [
        (None, {'fields': ['user']}),
        ('Book Information', {'fields': ['title', 'author', 'purchase_date', 'description', 'price']}),
    ]

    class Meta:
        model = SellPost