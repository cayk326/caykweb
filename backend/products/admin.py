from django.contrib import admin
from .models import Category, Book, Grocery, Hello, ReadBook

# Register your models here.

admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Grocery)
admin.site.register(Hello)
admin.site.register(ReadBook)