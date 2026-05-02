from django.contrib import admin
from .models import Commande

@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = ['id', 'client', 'livreur', 'dateCommande', 'total', 'status']
    search_fields = ['client__nom', 'client__prenom']
    list_filter = ['status', 'modePaiement']