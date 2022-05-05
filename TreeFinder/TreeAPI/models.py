# models.py
from xmlrpc.client import boolean
from django.db import models
import uuid
from datetime import datetime
from django_google_maps import fields as map_fields

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# from django.contrib.auth.models import AbstractUser


class UserProfile(models.Model):
    # REQUIRED_FIELDS = ('user','address','date_birth')
    user = models.OneToOneField(User, related_name='profile', unique=True, on_delete=models.CASCADE)
    address = models.CharField(max_length=60)
    date_birth = models.DateField(auto_now=False, auto_now_add=False)

    # USERNAME_FIELD = 'username'

    def __str__(self):
        return str(self.user.username)

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

# class User(models.Model):
    # https://docs.djangoproject.com/en/4.0/ref/models/fields/#uuidfield
    # pass
    # user_id = models.UUIDField(
    #     'user_id',
    #     primary_key = True,
    #     default = uuid.uuid4,
    #     editable = False
    # )
    # # https://docs.djangoproject.com/en/4.0/ref/models/fields/#charfield
    # username = models.CharField(max_length=30)
    # address = models.CharField(max_length=60)
    # # https://docs.djangoproject.com/en/4.0/ref/models/fields/#datefield
    # date_birth = models.DateField(auto_now=False, auto_now_add=False)

    # def __str__(self):
    #     return str(self.username)

class Tree(models.Model):
    tree_ID = models.UUIDField('tree_ID', primary_key=True, default=uuid.uuid4, editable=False)
    lat = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    long = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    Type = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.Type + " [" + str(self.lat) + "," + str(self.long) + "]"

class Journey(models.Model):
    title = models.CharField(max_length=50, default="Journey Title")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transportType = models.CharField(max_length=20)
    date = models.DateField()
    success = models.BooleanField()
    tree = models.ForeignKey(Tree, on_delete=models.CASCADE, null=True)
    duration = models.DurationField()
    distance = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.title + " | " + self.date.strftime("%d-%b-%Y")

