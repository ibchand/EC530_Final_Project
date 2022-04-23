# views.py
from rest_framework import viewsets

from .serializers import UserSerializer, TreeSerializer, JourneySerializer
from .models import User, Tree, Journey

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('user_id')
    serializer_class = UserSerializer

class TreeViewSet(viewsets.ModelViewSet):
    queryset = Tree.objects.all().order_by('tree_ID')
    serializer_class = TreeSerializer

class JourneyViewSet(viewsets.ModelViewSet):
    queryset = Journey.objects.all().order_by('date')
    serializer_class = JourneySerializer