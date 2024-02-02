from django.db import models
from django.utils.text import slugify
from django_quill.fields import QuillField
from django.utils import timezone


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True, blank=True,editable=False)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Award(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True,editable=False)
    year = models.IntegerField()
    date = models.DateField(auto_now=False, auto_now_add=False,default=timezone.now)
    location = models.CharField(max_length=200)
    description = QuillField()
    categories = models.ManyToManyField(Category, related_name='awards')
    active_award = models.BooleanField(default=False,)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


