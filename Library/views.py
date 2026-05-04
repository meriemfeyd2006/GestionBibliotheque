from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import render, redirect

from Clients.models import Client


def index(request):
    return render(request, 'library/index.html')


def connexion(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()

        if not email or not password:
            messages.error(request, 'Veuillez saisir un email et un mot de passe.')
        else:
            try:
                client = Client.objects.get(email=email)
                password_match = (
                    client.motDePasse == password or
                    check_password(password, client.motDePasse)
                )
                if password_match:
                    request.session['client_email'] = client.email
                    request.session['client_id'] = client.id
                    messages.success(request, f'Bienvenue de retour, {client.prenom or client.email} !')
                    return redirect('library-index')
                messages.error(request, 'Mot de passe incorrect. Veuillez réessayer.')
            except Client.DoesNotExist:
                messages.error(request, 'Aucun compte trouvé avec cet email. Veuillez vous inscrire.')

    return render(request, 'library/connexion.html')


def inscription(request):
    if request.method == 'POST':
        nom = request.POST.get('nom', '').strip()
        prenom = request.POST.get('prenom', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        adresse = request.POST.get('adresse', '').strip()
        telephone = request.POST.get('telephone', '').strip()

        if not all([nom, prenom, email, password, adresse, telephone]):
            messages.error(request, 'Tous les champs sont obligatoires.')
        elif Client.objects.filter(email=email).exists():
            messages.error(request, 'Un compte existe déjà avec cet email. Veuillez vous connecter.')
        else:
            client = Client(
                nom=nom,
                prenom=prenom,
                email=email,
                motDePasse=make_password(password),
                adresse=adresse,
                telephone=telephone,
            )
            client.save()
            messages.success(request, 'Inscription réussie. Vous pouvez maintenant vous connecter.')
            return redirect('connexion')

    return render(request, 'library/inscription.html')


def reserver_livre_view(request, livre_id):
    from Reservations.views import reserver_livre
    return reserver_livre(request, livre_id)


def recuperer_livre_view(request, reservation_id):
    from Reservations.views import recuperer_livre
    return recuperer_livre(request, reservation_id)


def mes_reservations_view(request):
    from Reservations.views import mes_reservations
    return mes_reservations(request)


def mes_emprunts_view(request):
    from Reservations.views import mes_emprunts
    return mes_emprunts(request)


def deconnexion(request):
    if request.method == 'POST':
        request.session.pop('client_email', None)
        request.session.pop('client_id', None)
        messages.success(request, 'Vous êtes déconnecté.')
    return redirect('library-index')
