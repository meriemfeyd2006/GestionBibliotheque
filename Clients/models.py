from django.db import models

class Client(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(max_length=191, unique=True)
    motDePasse = models.CharField(max_length=255)
    telephone = models.CharField(max_length=20)
    adresse = models.CharField(max_length=255)
    dateInscription = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'clients'

    def __str__(self):
        return f"Client: {self.prenom} {self.nom}"