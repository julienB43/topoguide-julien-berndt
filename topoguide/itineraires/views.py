from django.shortcuts import render, get_list_or_404, get_object_or_404

from .models import Itineraire, Sortie

def itineraire(request):
    itineraires = get_list_or_404(Itineraire)
    return render(request, 'itineraires/itineraires.html', {'itineraires': itineraires})

def sorties(request, itineraire_id):
    sorties = get_list_or_404(Sortie, pk=itineraire_id)
    return render(request, 'itineraires/sorties.html', {'sorties': sorties})