from django.db import models

class Utilisateur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(max_length=191, unique=True)
    motDePasse = models.CharField(max_length=255)
    telephone = models.CharField(max_length=20)

    class Meta:
        db_table = 'utilisateurs'