from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('api/clients/', views.api_clients, name='api_clients'),
    path('clients/add/', views.add_client, name='add_client'),
]