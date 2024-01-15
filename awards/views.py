# views.py
from rest_framework import generics
from .models import Award
from .serializers import AwardSerializer

class AwardListView(generics.ListAPIView):
    queryset = Award.objects.all()
    serializer_class = AwardSerializer

class AwardDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Award.objects.all()
    serializer_class = AwardSerializer
    lookup_field = "slug"
