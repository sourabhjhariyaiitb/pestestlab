from django.urls import path, include
from . import views
urlpatterns = [
    path('basicinfo', views.basicinfo, name='basicinfo'),
    # path('nginfo', views.NGForm, name='NGForm'),
    # path('factsheet', views.factsheet, name='factsheet'),
    # path('factsheet_dynamic', views.factsheet_dynamic, name='factsheet_dynamic'),
    # path('financial', views.financial, name='financial'),
    # path('output_indicators', views.output_indicators, name='output_indicators'),
]