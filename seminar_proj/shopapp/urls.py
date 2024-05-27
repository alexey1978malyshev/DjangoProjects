from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('index', views.index, name='index'),
    path('orders/<int:customer_id>', views.get_orders_by_customers_id, name='orders'),
    path('orders_by_time/<int:customer_id>', views.get_products, name='orders_by_time'),
    path('update_prod/<int:prod_id>', views.update_prod, name='update_prod'),
    path('upload/', views.upload_image, name='upload_image'),

]