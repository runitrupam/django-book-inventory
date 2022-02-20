from django.contrib import admin
from django.contrib.admin.decorators import register
from home_app.models import Book
# Register your models here.

admin.site.register(Book)