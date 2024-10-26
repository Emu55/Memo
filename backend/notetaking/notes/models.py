from django.db import models

# Create your models here.
class Memo(models.Model):
    title = models.CharField(max_length=100)
    message = models.CharField(max_length=255)
    date = models.DateTimeField()
