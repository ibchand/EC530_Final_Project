# models.py
from xmlrpc.client import boolean
from django.db import models
import uuid
from datetime import datetime

class User(models.Model):
    # https://docs.djangoproject.com/en/4.0/ref/models/fields/#uuidfield
    user_id = models.UUIDField(
        'user_id',
        primary_key = True,
        default = uuid.uuid4,
        editable = False
    )
    # https://docs.djangoproject.com/en/4.0/ref/models/fields/#charfield
    username = models.CharField(max_length=30)
    address = models.CharField(max_length=60)
    # https://docs.djangoproject.com/en/4.0/ref/models/fields/#datefield
    date_birth = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return str(self.username)

class Tree(models.Model):
    tree_ID = models.UUIDField('tree_ID', primary_key=True, default=uuid.uuid4, editable=False)
    lat = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    long = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    Type = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return "[" + str(self.lat) + "," + str(self.long) + "]"

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
        return self.title + " - " + self.date.strftime("%d-%b-%Y")