from django.db import models
from Utilisateurs.models import Utilisateur

class Client(Utilisateur):
    adresse = models.CharField(max_length=255)
    dateInscription = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'clients'

    def __str__(self):
        return f"Client: {self.prenom} {self.nom}"