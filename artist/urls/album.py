from artist.views import album
from django.urls import path

urlpatterns = [
    path('', album.AlbumListAPIView.as_view(),name="album-list"),
    path('<slug:slug>', album.AlbumDetailAPIView.as_view(),name="album-detail"),
]
