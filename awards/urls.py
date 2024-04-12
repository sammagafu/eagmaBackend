# urls.py
from django.urls import path
from .views import (
    AwardListView, AwardDetailView,ActiveAwardListAPIView
)

urlpatterns = [
    path('', AwardListView.as_view(), name='award-list-create'),
    path('active/', ActiveAwardListAPIView.as_view(), name='award-list-create'),
    path('<slug:slug>/', AwardDetailView.as_view(), name='award-detail'),
]
