from django.contrib import admin
from .models import Tree, Journey, UserProfile

admin.site.register(UserProfile)
admin.site.register(Tree)
admin.site.register(Journey)

