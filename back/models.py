from django.db import models
from django.db.models.base import Model

# Create your models here.

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    price = models.FloatField(max_length=10)
    date = models.DateField()
    publish = models.CharField(max_length=32)
    
