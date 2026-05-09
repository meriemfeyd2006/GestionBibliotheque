from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404

from Clients.models import Client
from Empruntes.models import Emprunt
from Reservations.models import Reservation
from Livres.models import Livre
from Commandes.models import Commande
from Paiements.models import Paiement
from Livreurs.models import Livreur
from Categories.models import Categorie
from .forms import ClientForm


def index(request):
    return render(request, 'admine/page_admin.html')


def clients(request):
    clients = Client.objects.all().order_by('-dateInscription')
    return render(request, 'admine/clients.html', {'clients': clients})


def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(request, 'admine/client_detail.html', {'client': client})


def client_edit(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return render(request, 'admine/clients.html', {'clients': Client.objects.all().order_by('-dateInscription')})
            return redirect('admin_clients')
    else:
        form = ClientForm(instance=client)
    return render(request, 'admine/client_edit.html', {'client': client, 'form': form})


def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('admin_clients')
    return redirect('admin_clients')


def livreurs(request):
    livreurs = Livreur.objects.all().order_by('nom')
    return render(request, 'admine/livreurs.html', {'livreurs': livreurs})


def commandes(request):
    commandes = Commande.objects.select_related('client', 'livreur').prefetch_related('livres').all().order_by('-dateCommande')
    return render(request, 'admine/commandes.html', {'commandes': commandes})


def empreinte(request):
    emprunts = Emprunt.objects.select_related('client', 'livre').all().order_by('-dateEmprunt')
    return render(request, 'admine/emprunts.html', {'emprunts': emprunts})


def reservations(request):
    reservations = Reservation.objects.select_related('client', 'livre').all().order_by('-dateReservation')
    return render(request, 'admine/reservations.html', {'reservations': reservations})


def paiements(request):
    paiements = Paiement.objects.select_related('client', 'livre').all().order_by('-datePaiement')
    return render(request, 'admine/paiements.html', {'paiements': paiements})


def livres(request):
    livres = Livre.objects.select_related('categorie').all().order_by('titre')
    return render(request, 'admine/livres.html', {'livres': livres})


def categories(request):
    categories = Categorie.objects.all().order_by('nom')
    return render(request, 'admine/categories.html', {'categories': categories})


def admin_logout(request):
    if request.method == 'POST':
        logout(request)
    return redirect('admin_dashboard')
