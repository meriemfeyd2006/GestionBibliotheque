from django.db import models
from Clients.models import Client
from Livreurs.models import Livreur
from Livres.models import Livre

class Commande(models.Model):
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='commandes'
    )
    livreur = models.ForeignKey(
        Livreur,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='commandes'
    )
    dateCommande = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, default='en_attente')
    modePaiement = models.CharField(max_length=50)
    livres = models.ManyToManyField(Livre, related_name='commandes')

    class Meta:
        db_table = 'commandes'

    def __str__(self):
        return f"Commande #{self.id} - {self.client}"