from rest_framework import serializers
from .models import Award, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class AwardSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    description_content = serializers.CharField(source='description', read_only=True)

    class Meta:
        model = Award
        fields = ('name','slug','date','year','location','description_content','active_award','categories')
