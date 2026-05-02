from django.db import models
from Categories.models import Categorie

class Livre(models.Model):
    titre = models.CharField(max_length=200)
    isbn = models.CharField(max_length=20, unique=True)
    anneePublication = models.IntegerField()
    langue = models.CharField(max_length=50)
    stock = models.IntegerField(default=0)
    Nom_Auteur = models.CharField(max_length=100)
    prixOriginal = models.DecimalField(max_digits=10, decimal_places=2)
    prix_symbolique = models.DecimalField(max_digits=10, decimal_places=2)
    categorie = models.ForeignKey(
        Categorie,
        on_delete=models.SET_NULL,
        null=True,
        related_name='livres'
    )

    class Meta:
        db_table = 'livres'

    def __str__(self):
        return self.titre