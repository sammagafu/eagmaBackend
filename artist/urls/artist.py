from artist.views import artist
from django.urls import path

urlpatterns = [
    path('', artist.ArtistListAPIView.as_view(),name="artist-list"),
    path('<slug:slug>', artist.ArtistDetailAPIView.as_view(),name="artist-detail"),
]
