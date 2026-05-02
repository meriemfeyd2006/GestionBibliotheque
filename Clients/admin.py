from django.contrib import admin
from .models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'nom', 'prenom', 'email', 'adresse', 'dateInscription']
    search_fields = ['nom', 'prenom', 'email']