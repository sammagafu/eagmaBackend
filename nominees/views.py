# views.py
from rest_framework import generics, permissions
from .models import Nominee, Vote
from .serializers import NomineeSerializer, VoteSerializer
from rest_framework import serializers


class NomineeListCreateView(generics.ListCreateAPIView):
    queryset = Nominee.objects.all()
    serializer_class = NomineeSerializer

class NomineeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Nominee.objects.all()
    serializer_class = NomineeSerializer

class VoteListCreateView(generics.ListCreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Ensure the user can vote only once in a specific category and award
        user = self.request.user
        category = serializer.validated_data['category']
        award = serializer.validated_data['award']

        if Vote.objects.filter(user=user, category=category, award=award).exists():
            raise serializers.ValidationError('You can vote only once in this category and award.')

        serializer.save(user=user)

class VoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
