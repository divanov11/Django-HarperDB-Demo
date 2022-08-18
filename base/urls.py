from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('profile/<str:pk>/', views.dev_profile, name="profile"),
    path('add/', views.add_profile, name="add"),

    path('profile/edit/<str:pk>/', views.update_profile, name="edit"),
    path('profile/delete/<str:pk>/', views.delete_profile, name="delete"),    
]