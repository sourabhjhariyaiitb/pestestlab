from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.map, name='map'),
    path('heir_map', views.heir_map, name='heir_map'),

]
