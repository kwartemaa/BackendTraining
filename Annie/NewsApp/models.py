from django.db import models
from django.utils import timezone


# Create your models here.
class News(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_published = models.DateField(default=timezone.now())

    def __str__(self):
        return self.author
