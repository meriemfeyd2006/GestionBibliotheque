from django.contrib import admin
from .models import Administrateur

@admin.register(Administrateur)
class AdministrateurAdmin(admin.ModelAdmin):
    list_display = ['id', 'nom', 'prenom', 'email']
    search_fields = ['nom', 'prenom', 'email']