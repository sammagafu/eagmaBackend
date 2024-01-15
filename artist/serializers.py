from rest_framework import serializers
from .models import Genre, Artist, Album, Song

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class SongSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()  # Nested serializer for the song genre

    class Meta:
        model = Song
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True)  # Nested serializer for the album songs

    class Meta:
        model = Album
        fields = '__all__'

class ArtistSerializer(serializers.ModelSerializer):
    albums = AlbumSerializer(many=True)  # Nested serializer for the artist albums

    class Meta:
        model = Artist
        fields = '__all__'
