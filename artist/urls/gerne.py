from artist.views import gerne
from django.urls import path

urlpatterns = [
    path('', gerne.GenreListAPIView.as_view(),name="song-list"),
    path('<slug:slug>', gerne.GenreDetailAPIView.as_view(),name="song-detail"),
]
