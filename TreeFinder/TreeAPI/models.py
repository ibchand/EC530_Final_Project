# models.py
from django.db import models

class Tree(models.Model):
    tree_ID = models.UUIDField(max_length = 12)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    Type = models.CharField(max_length=50)
    UserKey = models.UUIDField(max_length = 12)
    def __str__(self):
        return self.ID