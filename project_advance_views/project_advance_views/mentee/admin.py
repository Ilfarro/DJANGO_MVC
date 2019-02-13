from django.contrib import admin
from .models import Mentee
# Register your models here.

my_model = [Mentee]
admin.site.register(my_model)