from django.db import models
from django_resized import ResizedImageField
from django.utils.text import slugify
class Genre(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True, blank=True,editable=False)

    def __str__(self):
        return self.name

class Artist(models.Model):
    GENDER = [
        ("Female", "Female"),
        ("Male", "Male"),
    ]
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100,choices=GENDER,default="Female")
    slug = models.SlugField(max_length=200, unique=True, blank=True,editable=False)
    bio = models.TextField()
    photo = ResizedImageField(upload_to='artist_photos/',size=[800, 800], crop=['middle', 'center'],quality=100)
    website = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_photo(self):
        if self.photo:
            return 'https://api.eagma.co.tz' + self.photo.url
        return ''

class Album(models.Model):
    name = models.CharField(max_length=180)
    slug = models.SlugField(max_length=200, unique=True, blank=True,editable=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE,related_name="singer")
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True, blank=True,editable=False)
    title = models.CharField(max_length=200)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="album")
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    release_date = models.DateField()
    audio_file = models.URLField(blank=True)
    video_link = models.URLField(blank=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
