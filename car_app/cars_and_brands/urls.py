from django.urls import path
from . import views

urlpatterns = [
    path('', views.brand_list, name='brand_list'),
    path('new', views.new_brand, name='new_brand'),
    path('<int:brand_id>', views.brand_detail, name='brand_detail'),
    path('<int:brand_id>/edit', views.edit_brand, name='edit_brand'),
    path('<int:brand_id>/delete', views.delete_brand, name='delete_brand'),
    path('<int:brand_id>/cars', views.car_list, name='car_list'),
    path('<int:brand_id>/cars/new', views.new_car, name='new_car'),
    path('<int:brand_id>/cars/<int:car_id>', views.car_detail, name='car_detail'),
    path('<int:brand_id>/cars/<int:car_id>/edit', views.edit_car, name='edit_car'),
    path('<int:brand_id>/cars/<int:car_id>/delete', views.delete_car, name='delete_car'),
]