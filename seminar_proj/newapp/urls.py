from django.urls import path
from . import views

urlpatterns = [
    path('orel_reshka/', views.orel_reshka, name='orel_reshka'),
    path('cube/', views.cube, name='cube'),
    path('random_num/', views.random_num, name='random_num'),
]