from django.shortcuts import render, get_list_or_404

from .models import Itineraire

def itineraire(request):
    itineraires = get_list_or_404(Itineraire)
    return render(request, 'itineraires/itineraires.html', {'itineraires': itineraires})