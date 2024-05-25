from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('orel_reshka/<int:count>', views.orel_reshka, name='orel_reshka'),
    path('cube/<int:count>', views.cube, name='cube'),
    path('random_num/<int:count>', views.random_num, name='random_num'),
    path('get_last_val/', views.get_last_val, name='get_last_val'),
    path('choice_game/', views.choice_game, name='choice_game'),
]