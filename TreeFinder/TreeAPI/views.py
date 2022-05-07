# views.py
from rest_framework import viewsets
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.shortcuts import render

from .serializers import TreeSerializer, JourneySerializer
# from .serializers import UserProfileSerializer
from .models import User, Tree, Journey

from django.template import loader

# Data Prcocessing
import csv
import json
from django.utils import timezone
import os

# class UserProfileViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all().order_by('username')
#     serializer_class = UserProfileSerializer

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

    trees = Tree.objects.all()

    new_array = []

    for count, tree in enumerate(trees):
        if count % 128 == 0:
            new_array.append(tree)


    context = {
        'trees': new_array
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

def generate_trees(request):
    new_tree = Tree(lat="42", long="71", Type="UNKNOWN")

    new_tree.save()

    with open('Trees.csv', newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',',)

        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                new_tree = Tree(tree_ID=float(row[2]), lat=float(row[1]), long=float(row[0]), Type="Unknown")
                new_tree.save()
    return HttpResponse("Hello, this will take about an hour :)")
    

def chart_map(request):
    template = loader.get_template('TreeAPI/chart_map.html')

    trees = Tree.objects.all()

    new_array = []

    for count, tree in enumerate(trees):
        if count % 64 == 0:
            tree.long = tree.long * -1
            new_array.append(tree)


    context = {
        'trees': new_array
    }
    return HttpResponse(template.render(context, request))
