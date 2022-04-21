from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Itineraire, Sortie
from .form import SortieForm

def itineraire(request):
    itineraires = get_list_or_404(Itineraire)
    return render(request, 'itineraires/itineraires.html', {'itineraires': itineraires})

def sorties(request, itineraire_id):
    sorties = get_list_or_404(Sortie, pk=itineraire_id)
    return render(request, 'itineraires/sorties.html', {'sorties': sorties})

def sortie(request, user_id):
    sortie = get_object_or_404(Sortie, pk=user_id)
    return render(request, 'itineraires/sortie_detail.html', {'sortie': sortie})

@login_required
def nouvelle_sortie(request):  
    if request.method == 'GET':
        form = SortieForm()
    elif request.method == 'POST':
        form = SortieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('itineraires')
    return render(request,'itineraires/nouvelle_sortie.html', {'form': form})

@login_required
def modif_sortie(request, user_id):
    sortie = Sortie.objects.get(pk=user_id)
    if request.method == 'GET':
        form = SortieForm(instance=sortie)
    elif request.method == 'POST':
        form = SortieForm(request.POST, instance=sortie)
        if form.is_valid():
            form.save()
            return redirect('itineraires')
    return render(request, 'itineraires/modif_sortie.html', {'form': form})