from django.contrib.auth import logout
from django.shortcuts import render, redirect

from Clients.models import Client


def index(request):
    return render(request, 'admine/page_admin.html')


def clients(request):
    clients = Client.objects.all().order_by('-dateInscription')
    return render(request, 'admine/clients.html', {'clients': clients})


def livreurs(request):
    return render(request, 'admine/livreurs.html')


def commandes(request):
    return render(request, 'admine/commandes.html')


def empreinte(request):
    return render(request, 'admine/empreinte.html')


def reservations(request):
    return render(request, 'admine/reservations.html')


def paiements(request):
    return render(request, 'admine/paiements.html')


def admin_logout(request):
    if request.method == 'POST':
        logout(request)
    return redirect('admin_dashboard')
