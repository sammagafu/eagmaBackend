from django.db import models

# Create your models here.
class Award(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    location = models.IntegerField()
    description = models.TextField()

class Category(models.Model):
    name = models.CharField(max_length=100)

