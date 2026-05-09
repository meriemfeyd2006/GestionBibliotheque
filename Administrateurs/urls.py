from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='admin_dashboard'),
    path('clients/', views.clients, name='admin_clients'),
    path('clients/<int:pk>/', views.client_detail, name='admin_client_detail'),
    path('clients/<int:pk>/edit/', views.client_edit, name='admin_client_edit'),
    path('clients/<int:pk>/delete/', views.client_delete, name='admin_client_delete'),
    path('livreurs/', views.livreurs, name='admin_livreurs'),
    path('commandes/', views.commandes, name='admin_commandes'),
    path('empreinte/', views.empreinte, name='admin_emprunts'),
    path('reservations/', views.reservations, name='admin_reservations'),
    path('livres/', views.livres, name='admin_livres'),
    path('categories/', views.categories, name='admin_categories'),
    path('logout/', views.admin_logout, name='admin_logout'),
]
