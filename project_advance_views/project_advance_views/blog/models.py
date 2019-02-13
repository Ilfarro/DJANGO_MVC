from django.db import models
from django.utils import timezone 

class Blog_post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    comment_count = models.CharField(max_length=255)
    picture = models.CharField(max_length=255)

    def __str__(self):
        return self.title