from django.db import models
from Clients.models import Client
from Livres.models import Livre

class Emprunt(models.Model):
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='emprunts'
    )
    livre = models.ForeignKey(
        Livre,
        on_delete=models.CASCADE,
        related_name='emprunts'
    )
    dateEmprunt = models.DateField(auto_now_add=True)
    dateRetourPrevue = models.DateField()
    dateRetourReelle = models.DateField(null=True, blank=True)
    statut = models.CharField(
        max_length=20,
        choices=[('en_cours', 'En cours'), ('rendu', 'Rendu'), ('en_retard', 'En retard')],
        default='en_cours'
    )

    class Meta:
        db_table = 'emprunts'

    def __str__(self):
        return f"Emprunt #{self.id} - {self.client} - {self.livre}"