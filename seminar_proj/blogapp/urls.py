from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_author', views.create_author, name='create_author'),

]