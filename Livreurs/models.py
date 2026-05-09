from django.db import models

class Livreur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(max_length=191, unique=True)
    motDePasse = models.CharField(max_length=255)
    telephone = models.CharField(max_length=20)
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