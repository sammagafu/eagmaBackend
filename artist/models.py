from django.db import models
from django_quill.fields import QuillField
from django_resized import ResizedImageField
class Genre(models.Model):
    name = models.CharField(max_length=100)

class Artist(models.Model):
    name = models.CharField(max_length=100)
    bio = QuillField()
    photo = ResizedImageField(upload_to='artist_photos/',size=[800, 800], crop=['middle', 'center'],quality=100)
    website = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
class Album(models.Model):
    name = models.CharField(max_length=180)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    album = models.ForeignKey(Album, on_delete=models.CASCADE,)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    release_date = models.DateField()
    genre = models.CharField(max_length=50)
    audio_file = models.URLField(blank=True)
    video_link = models.URLField(blank=True)

    def __str__(self):
        return self.title
