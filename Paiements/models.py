from django.db import models
from Clients.models import Client
from Livres.models import Livre

class Paiement(models.Model):
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='paiements'
    )
    livre = models.ForeignKey(
        Livre,
        on_delete=models.CASCADE,
        related_name='paiements'
    )
    montant = models.FloatField()
    datePaiement = models.DateField(auto_now_add=True)
    methode = models.CharField(max_length=50)

    class Meta:
        db_table = 'paiements'

    def __str__(self):
        return f"Paiement #{self.id} - {self.montant} DH"