from django.db import models
from awards.models import Award,Category
from artist.models import Artist,Song

# Create your models here.
class Nominee(models.Model):
    award = models.ForeignKey(Award, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_winner = models.BooleanField(default=False)

class Vote(models.Model):
    user = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    nominee = models.ForeignKey(Nominee, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'category')
