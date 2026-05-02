from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404

from Clients.models import Client
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
