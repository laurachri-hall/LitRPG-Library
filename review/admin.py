from django.contrib import admin
from .models import Book, Review, Comment

# Register your models here.
admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Comment)