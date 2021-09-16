from django.contrib import admin
from django.db import models
from .models import SellPost, PostImage, PreferredBook, ExchangePost



class PostImageAdmin(admin.StackedInline):
    model = PostImage


@admin.register(SellPost)
class SellPostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    fieldsets = [
        (None, {'fields': ['user']}),
        ('Book Information', {'fields': ['title', 'author', 'purchase_date', 'description', 'price']}),
    ]
    search_fields = ('title', 'user')

    class Meta:
        model = SellPost



# @admin.register(PreferredBook)
# class PreferredBookAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ('Book Information', {'fields': ['title', 'author', 'edition', 'publisher']}),
#     ]
#     search_fields = ('title', 'author')

#     class Meta:
#         model = PreferredBook

admin.site.register(PreferredBook)

@admin.register(ExchangePost)
class ExchangePostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['user']}),
        ('Book Information', {'fields': ['title', 'author', 'purchase_date', 'description']}),
    ]
    search_fields = ('title', 'user')

    class Meta:
        model = ExchangePost