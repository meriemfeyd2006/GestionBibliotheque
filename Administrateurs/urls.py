from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='admin_dashboard'),
    path('clients/', views.clients, name='admin_clients'),
    path('livreurs/', views.livreurs, name='admin_livreurs'),
    path('commandes/', views.commandes, name='admin_commandes'),
    path('empreinte/', views.empreinte, name='admin_empreinte'),
    path('reservations/', views.reservations, name='admin_reservations'),
    path('paiements/', views.paiements, name='admin_paiements'),
    path('logout/', views.admin_logout, name='admin_logout'),
]
