from rest_framework import serializers
from .models import Genre, Artist, Album, Song

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name', 'slug')

class ArtistSerializer(serializers.ModelSerializer):
    albums = serializers.SerializerMethodField()

    class Meta:
        model = Artist
        fields = ('id', 'name','gender', 'slug', 'bio', 'photo', 'website', 'created_at', 'albums','get_photo')

    def get_albums(self, obj):
        albums = obj.singer.all()
        return AlbumSerializer(albums, many=True).data

class AlbumSerializer(serializers.ModelSerializer):
    songs = serializers.SerializerMethodField()

    class Meta:
        model = Album
        fields = ('id', 'name', 'slug', 'artist', 'songs')

    def get_songs(self, obj):
        songs = obj.album.all()
        return SongSerializer(songs, many=True).data

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('id', 'artist', 'slug', 'title', 'album', 'genre', 'release_date', 'audio_file', 'video_link')

