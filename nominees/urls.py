# awards/urls.py
from django.urls import path
from .views import (
    NomineeListCreateView, NomineeDetailView,
    VoteListCreateView, VoteDetailView
)

urlpatterns = [
    path('', NomineeListCreateView.as_view(), name='nominee-list-create'),
    path('<int:pk>/', NomineeDetailView.as_view(), name='nominee-detail'),
    path('votes/', VoteListCreateView.as_view(), name='vote-list-create'),
    path('votes/<int:pk>/', VoteDetailView.as_view(), name='vote-detail'),
]
