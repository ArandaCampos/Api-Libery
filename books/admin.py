from django.contrib import admin
from .models import booksModel

# Register your models here.
@admin.register(booksModel)
class adminBooks(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'pages', 'publisher']