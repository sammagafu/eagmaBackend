# serializers.py
from rest_framework import serializers
from .models import Nominee, Vote

class NomineeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nominee
        depth = 1
        fields = '__all__'

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'
        read_only_fields = ('user',)
