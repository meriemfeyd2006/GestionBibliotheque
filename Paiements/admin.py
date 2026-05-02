from django.contrib import admin
from .models import Paiement

@admin.register(Paiement)
class PaiementAdmin(admin.ModelAdmin):
    list_display = ['id', 'client', 'livre', 'montant', 'datePaiement', 'methode']
    search_fields = ['client__nom', 'livre__titre']
    list_filter = ['methode']