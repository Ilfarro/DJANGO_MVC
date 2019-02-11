from django.contrib import admin
from .models import Direksi, Mentee, Mata_pelajaran, Mentor, Challenge, Live_code
# Register your models here.

my_model = [Direksi, Mentee, Mata_pelajaran, Mentor, Challenge, Live_code]
admin.site.register(my_model)