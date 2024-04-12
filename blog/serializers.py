from rest_framework import serializers
from .models import BlogPost, Category

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        depth = 1
        fields = ('id', 'title','slug','photo','category', 'content', 'author', 'created_at', 'updated_at','get_photo')

class CategorySerializer(serializers.ModelSerializer):
    blogpost_set = BlogPostSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'blogpost_set')
