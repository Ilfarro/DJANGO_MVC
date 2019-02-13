from django.contrib import admin
from .models import Blog_post
# Register your models here.

my_model = [Blog_post]
admin.site.register(my_model)