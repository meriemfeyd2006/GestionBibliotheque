from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['id', 'client', 'livre', 'dateReservation', 'dateExpiration', 'statut']
    search_fields = ['client__nom', 'livre__titre']
    list_filter = ['statut']