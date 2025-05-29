from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),
     path('add-inquiry/', views.add_inquiry, name='add_inquiry'),

     # ...existing code...
    path('car/<int:car_id>/edit/', views.car_edit, name='car_edit'),
    path('car/<int:car_id>/delete/', views.car_delete, name='car_delete'),
    path('car/add/', views.car_add, name='car_add'),
]

