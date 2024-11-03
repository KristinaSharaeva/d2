from django.urls import path
from . import views

urlpatterns = [
    path('clients/', views.client_list, name='client_list'),
    path('clients/create/', views.create_client, name='create_client'),
    path('clients/update/<int:client_id>/', views.update_client, name='update_client'),
    path('clients/delete/<int:client_id>/', views.delete_client, name='delete_client'),
]
