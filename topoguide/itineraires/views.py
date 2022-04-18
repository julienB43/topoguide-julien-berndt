from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse

from .models import Itineraire

def itineraires(request):
    
    itineraire = get_list_or_404(Itineraire)
    
    return render(request, 'itineraires/itineraires.html', {'itineraire': itineraire})
