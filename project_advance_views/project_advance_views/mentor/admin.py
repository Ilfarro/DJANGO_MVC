from django.contrib import admin
from .models import Mentor
# Register your models here.

my_model = [Mentor]
admin.site.register(my_model)