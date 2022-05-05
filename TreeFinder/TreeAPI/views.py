# views.py
from rest_framework import viewsets
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.shortcuts import render

from .serializers import UserProfileSerializer, TreeSerializer, JourneySerializer
from .models import User, Tree, Journey

from django.template import loader

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('username')
    serializer_class = UserProfileSerializer

class TreeViewSet(viewsets.ModelViewSet):
    queryset = Tree.objects.all().order_by('tree_ID')
    serializer_class = TreeSerializer

class JourneyViewSet(viewsets.ModelViewSet):
    queryset = Journey.objects.all().order_by('date')
    serializer_class = JourneySerializer

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def home(request):
    template = loader.get_template('TreeAPI/home.html')
    context = {
        'dummy': "Hello World from a Template!"
    }
    return HttpResponse(template.render(context, request))
    # return HttpResponse("Hello, world.")

def auth(request):
    template = loader.get_template('TreeAPI/auth.html')
    context = {
        'dummy': "Authentication Screen!"
    }
    return HttpResponse(template.render(context, request))
    # return HttpResponse("Hello, world.")

def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.my_mapbox_access_token'
    return render(request, 'default.html', 
                  'pk.eyJ1IjoiYmJyZXdlcjEiLCJhIjoiY2wydDY2NjhhMDA0bzNqbzBua3dmZW5sYyJ9.LfFgtGqHdycL6ZFNYsPpQg')