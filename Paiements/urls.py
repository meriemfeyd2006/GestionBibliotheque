from django.urls import path
from . import views

urlpatterns = [
    path('admin_paiements/', views.admin_paiements, name='admin_paiements'),
]
