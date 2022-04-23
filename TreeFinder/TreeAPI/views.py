# views.py
from rest_framework import viewsets

from .serializers import TreeSerializer
from .models import Tree


class TreeViewSet(viewsets.ModelViewSet):
    queryset = Tree.objects.all().order_by('tree_ID')
    serializer_class = TreeSerializer