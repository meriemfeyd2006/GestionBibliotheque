from django.db import models
from Utilisateurs.models import Utilisateur

class Administrateur(Utilisateur):

    class Meta:
        db_table = 'administrateurs'

    def __str__(self):
        return f"Admin: {self.prenom} {self.nom}"