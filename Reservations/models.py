from django.db import models
from Clients.models import Client
from Livres.models import Livre

class Reservation(models.Model):
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='reservations'
    )
    livre = models.ForeignKey(
        Livre,
        on_delete=models.CASCADE,
        related_name='reservations'
    )
    dateReservation = models.DateField(auto_now_add=True)
    dateExpiration = models.DateField()
    statut = models.CharField(
        max_length=20,
        choices=[('active', 'Active'), ('expiree', 'Expirée'), ('annulee', 'Annulée')],
        default='active'
    )

    class Meta:
        db_table = 'reservations'

    def __str__(self):
        return f"Réservation #{self.id} - {self.client} - {self.livre}"