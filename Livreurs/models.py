from django.db import models
from Utilisateurs.models import Utilisateur

class Livreur(Utilisateur):
    vehicule = models.CharField(max_length=100)
    zone = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=[('disponible', 'Disponible'), ('en_livraison', 'En livraison')],
        default='disponible'
    )

    class Meta:
        db_table = 'livreurs'

    def __str__(self):
        return f"Livreur: {self.prenom} {self.nom}"