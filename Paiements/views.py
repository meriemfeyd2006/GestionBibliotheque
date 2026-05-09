from django.shortcuts import render

def admin_paiements(request):
	from .models import Paiement
	paiements = Paiement.objects.all()
	return render(request, 'admine/paiements.html', {'paiements': paiements})
