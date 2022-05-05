from django.contrib import admin
from .models import User, Tree, Journey
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

admin.site.register(UserProfile)
admin.site.register(Tree)
admin.site.register(Journey)

class MapTestAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {
            'widget': map_widgets.GoogleMapsAddressWidget(attrs={'data-map-type': 'roadmap'})
        },
    }