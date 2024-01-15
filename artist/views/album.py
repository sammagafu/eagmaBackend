from rest_framework import generics
from artist.models import Album
from artist.serializers import AlbumSerializer

class AlbumListAPIView(generics.ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class AlbumDetailAPIView(generics.RetrieveAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    lookup_field = "slug"
