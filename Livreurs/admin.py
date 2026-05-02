from django.contrib import admin
from .models import Livreur

@admin.register(Livreur)
class LivreurAdmin(admin.ModelAdmin):
    list_display = ['id', 'nom', 'prenom', 'vehicule', 'zone', 'status']
    search_fields = ['nom', 'prenom']
    list_filter = ['status', 'zone']