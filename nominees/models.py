from django.db import models
from awards.models import Award,Category
from artist.models import Artist,Song
from django.conf import settings
from django.utils import timezone

# django.utils.timezone.now


# Create your models here.
class Nominee(models.Model):
    award = models.ForeignKey(Award, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_winner = models.BooleanField(default=False)

class Vote(models.Model):
    award = models.ForeignKey(Award, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name="votingCategory")
    voted_nominee = models.ForeignKey(Nominee, on_delete=models.CASCADE,related_name="nominiee")  # If you have a Nominee model
    voted_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        unique_together = ('user', 'category','award')
