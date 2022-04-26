# views.py
from rest_framework import viewsets
from django.http import HttpResponse


from .serializers import UserSerializer, TreeSerializer, JourneySerializer
from .models import User, Tree, Journey

from django.template import loader

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('user_id')
    serializer_class = UserSerializer

class TreeViewSet(viewsets.ModelViewSet):
    queryset = Tree.objects.all().order_by('tree_ID')
    serializer_class = TreeSerializer

class JourneyViewSet(viewsets.ModelViewSet):
    queryset = Journey.objects.all().order_by('date')
    serializer_class = JourneySerializer

def home(request):
    template = loader.get_template('TreeAPI/home.html')
    context = {
        'dummy': "Hello World from a Template!"
    }
    return HttpResponse(template.render(context, request))
    # return HttpResponse("Hello, world.")