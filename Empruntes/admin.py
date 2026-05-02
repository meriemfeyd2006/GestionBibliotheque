from django.contrib import admin
from .models import Emprunt

@admin.register(Emprunt)
class EmpruntAdmin(admin.ModelAdmin):
    list_display = ['id', 'client', 'livre', 'dateEmprunt', 'dateRetourPrevue', 'statut']
    search_fields = ['client__nom', 'livre__titre']
    list_filter = ['statut']