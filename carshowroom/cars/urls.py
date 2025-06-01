from django.urls import path
from . import views
from .views import CustomLoginView
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', views.home, name='home'),
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),
     path('add-inquiry/', views.add_inquiry, name='add_inquiry'),

     # ...existing code...
    path('car/<int:car_id>/edit/', views.car_edit, name='car_edit'),
    path('car/<int:car_id>/delete/', views.car_delete, name='car_delete'),
    path('car/add/', views.car_add, name='car_add'),
      path('inquiries/', views.inquiries_list, name='inquiries_list'),
      path('inquiries/', views.inquiries_list, name='inquiries_list'),
    path('inquiries/delete/<int:inquiry_id>/', views.delete_inquiry, name='delete_inquiry'),
     path('login/', CustomLoginView.as_view(), name='login'),
     path('logout/', LogoutView.as_view(next_page='/'), name='logout'),

]

