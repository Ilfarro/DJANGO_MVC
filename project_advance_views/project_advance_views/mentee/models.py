from django.db import models
from django.utils import timezone 

class Mentee(models.Model):
    name = models.CharField(max_length=255)
    quote = models.TextField(max_length=255)
    picture = models.CharField(max_length=255)

    def __str__(self):
        return self.name