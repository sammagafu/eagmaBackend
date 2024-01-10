
from rest_framework import serializers
from .models import BlogPost,Category


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ('id', 'title', 'content', 'author', 'created_at', 'updated_at')

class CategorySerializer(serializers.ModelSerializer):
    blog_posts = BlogPostSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'blog_posts')