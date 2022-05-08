# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'userprofiles', views.UserProfileViewSet)
router.register(r'trees', views.TreeViewSet)
router.register(r'journeys', views.JourneyViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('home/', views.home, name='home'),
    path('tree-map/', views.chart_map, name='tree-map'),
    path('generate-trees/', views.generate_trees, name='generate-trees'),
    path('journey/', views.journey, name='journey'),
    path('past-journey/', views.past_journey, name='past-journey'),
    path('auth/', views.auth, name='auth'),
    path('auth/signup/', views.SignUp.as_view(), name='signup')
]