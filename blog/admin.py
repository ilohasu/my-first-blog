from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Post, Diary, Category

admin.site.register(Post)
admin.site.register(Diary)
admin.site.register(Category)