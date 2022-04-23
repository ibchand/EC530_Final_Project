# serializers.py
from rest_framework import serializers

from .models import Journey, Tree

class TreeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tree
        fields = ('tree_ID', 'lat', 'long', 'Type', 'UserKey')

class JourneySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Journey
        fields = ('UserKey', 'transportType', 'date', 'success', 'tree', 'duration', 'distance')