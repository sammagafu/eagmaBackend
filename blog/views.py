from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer

class CategoryWithBlogPostsView(generics.ListAPIView):
    queryset = Category.objects.prefetch_related('blogpost_set')
    serializer_class = CategorySerializer