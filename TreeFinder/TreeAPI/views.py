# views.py
from rest_framework import viewsets
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.shortcuts import render

from .serializers import TreeSerializer, JourneySerializer
from .serializers import UserProfileSerializer
from .models import User, Tree, Journey, UserProfile, JourneyForm

from django.template import loader
import datetime

# Data Prcocessing
import csv
import json
from django.utils import timezone
import os
import random

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
    favorited_tree_id = request.POST.get('favoriteButton', None)

    if (favorited_tree_id == None):
        if (request.method == 'POST'):
            form = JourneyForm(request.POST)
            if (form.is_valid()):
                print(form['title'])
                form.save()
    else:
        # print('HANDLING FAVORITE TREE')
        requested_tree = Tree.objects.filter(tree_ID=favorited_tree_id)[0]
        user_profile = UserProfile.objects.filter(user=request.user)
        user_profile[0].favorite_trees.add(requested_tree)
        # user_profile.save()
    

    # JourneyForm Handling
    # journey_data = request.POST.get('journeyFormButton', None)
    # print("JOURNEY DATA: " + journey_data)
    # if (journey_data != None):
    #     journey_form = JourneyForm(**form_args)
    #     print(journey_form)
    #     if JourneyForm.is_valid():
    #         yazilar = journey_form.save(commit=True)
    
    # print("------------: " + journey_data)
    # f = JourneyForm(request.POST, initial=data)
    # print(f)

    template = loader.get_template('TreeAPI/home.html')

    context = {}

    try:
        user_profile = UserProfile.objects.filter(user=request.user)
        user_journeys = Journey.objects.filter(user=request.user)

        context['user_trees'] = user_profile[0].favorite_trees.all()
        context['user_journeys'] = user_journeys
    except:
        context['user_trees'] = []
        context['user_journeys'] = []

    trees = Tree.objects.all()

    new_array = []

    # for count, tree in enumerate(trees):
    #     if count % 128 == 0:
    #         new_array.append(tree)


    # context['trees'] = new_array
    # print(random.sample(list(trees),10))
    context['random_trees'] = random.sample(list(trees), 5)
    

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
            elif line_count % 128 == 0:
                new_tree = Tree(tree_ID=float(row[2]), lat=float(row[1]), long=float(row[0]), Type="Unknown")
                new_tree.save()
            line_count += 1
    return HttpResponse("Hello, the current divison factor is 128, resulting in 1577 trees. Change this setting in TreeFinder/TreeAPI/views.py->generate_trees view")
    

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

def journey(request):
    context = {}

    template = loader.get_template('TreeAPI/journey.html')

    requested_tree_id = request.POST.get('journeyButton', None)

    print(requested_tree_id)

    requested_tree = Tree.objects.filter(tree_ID=requested_tree_id)[0]

    if (requested_tree_id != None):
        requested_tree = Tree.objects.filter(tree_ID=requested_tree_id)[0]
        context['tree'] = requested_tree
        context['tree_id'] = requested_tree_id

    form = JourneyForm(initial={'user': request.user, 'tree': requested_tree})

    context['journeyForm'] = form

    return HttpResponse(template.render(context, request))

def past_journey(request):
    context = {}

    template = loader.get_template('TreeAPI/past_journey.html')

    requested_journey_id = request.POST.get('past_journeyButton', None)

    if (requested_journey_id != None):
        requested_journey = Journey.objects.filter(journey_ID=requested_journey_id)[0]
        context['journey'] = requested_journey

    return HttpResponse(template.render(context, request))
