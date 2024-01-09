from django.db import models
from django_quill.fields import QuillField


# Create your models here.
class Award(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    location = models.IntegerField()
    description = QuillField()

class Category(models.Model):
    name = models.CharField(max_length=100)

