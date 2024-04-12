from artist.views import song
from django.urls import path

urlpatterns = [
    path('', song.SongListAPIView.as_view(),name="song-list"),
    path('<slug:slug>', song.SongDetailAPIView.as_view(),name="song-detail"),
]
