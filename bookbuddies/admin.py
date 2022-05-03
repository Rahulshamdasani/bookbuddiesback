from django.contrib import admin
from .models import Book, Exchange
@admin.register(Book)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['isbn','title', 'author', 'year', 'publisher', 'url']

admin.site.register(Exchange)