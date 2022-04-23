# views.py
from rest_framework import viewsets

from .serializers import JourneySerializer, TreeSerializer
from .models import Tree, Journey


class TreeViewSet(viewsets.ModelViewSet):
    queryset = Tree.objects.all().order_by('tree_ID')
    serializer_class = TreeSerializer

class JourneyViewSet(viewsets.ModelViewSet):
    queryset = Journey.objects.all().order_by('date')
    serializer_class = JourneySerializer