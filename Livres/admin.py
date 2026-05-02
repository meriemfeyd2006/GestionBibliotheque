from django.contrib import admin
from .models import Livre

@admin.register(Livre)
class LivreAdmin(admin.ModelAdmin):
    list_display = ['id', 'titre', 'Nom_Auteur', 'isbn', 'stock', 'prixOriginal', 'categorie']
    search_fields = ['titre', 'Nom_Auteur', 'isbn']
    list_filter = ['categorie', 'langue']