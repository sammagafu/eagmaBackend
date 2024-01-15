from django.urls import path, include

urlpatterns = [
    path("album/", include('artist.urls.album')),  
    path("artist/", include('artist.urls.artist')),  
    path("gerne/", include('artist.urls.gerne')),  
    path("song/", include('artist.urls.song')),  
]