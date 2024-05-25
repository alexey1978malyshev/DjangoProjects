from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_author', views.create_author, name='create_author'),
    path('add_author', views.create_author_by_form, name='add_author'),
    path('delete_author/<int:id_author>/', views.delete_author_by_id, name='delete_author')

]