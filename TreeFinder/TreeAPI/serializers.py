# serializers.py
from rest_framework import serializers

from .models import Tree

class TreeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tree
        fields = ('tree_ID', 'lat', 'long', 'Type', 'UserKey')