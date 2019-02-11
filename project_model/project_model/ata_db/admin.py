from django.contrib import admin
from .models import Mentee, Blog_post
# Register your models here.

my_model = [Blog_post, Mentee]
admin.site.register(my_model)