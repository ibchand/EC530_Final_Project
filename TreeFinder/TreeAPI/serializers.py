# serializers.py
from rest_framework import serializers

from .models import User, Tree, Journey

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = (
            'user_id',
            'username',
            'address',
            'date_birth',
        )

class TreeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tree
        fields = ('tree_ID', 'lat', 'long', 'Type', 'user')

class JourneySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Journey
        fields = ('title', 'user', 'transportType', 'date', 'success', 'tree', 'duration', 'distance')