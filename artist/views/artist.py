from rest_framework import generics
from artist.models import Artist
from artist.serializers import ArtistSerializer

class ArtistListAPIView(generics.ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class ArtistDetailAPIView(generics.RetrieveAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    lookup_field = "slug"
