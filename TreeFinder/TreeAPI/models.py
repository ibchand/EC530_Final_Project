# models.py
from xmlrpc.client import boolean
from django.db import models
import uuid
from datetime import datetime

class Tree(models.Model):
    tree_ID = models.UUIDField('tree_ID', primary_key=True, default=uuid.uuid4, editable=False)
    lat = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    long = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    Type = models.CharField(max_length=50)
    UserKey = models.UUIDField('UserKey', primary_key=False, default=uuid.uuid4, editable=False)
    def __str__(self):
        return self.Type

class Journey(models.Model):
    UserKey = models.UUIDField(max_length=12)
    transportType = models.CharField(max_length=20)
    date = models.DateField()
    success = models.BooleanField()
    tree = models.OneToOneField(Tree, null=True, on_delete=models.CASCADE)
    duration = models.DurationField()
    distance = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.date.strftime("%d-%b-%Y")