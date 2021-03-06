from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Itineraire, Sortie
from .form import SortieForm


def itineraire(request):
    """
    Vue sur la liste des itineraires proposés par le site:
    
    Args:
        request: la requête demandée
        
    Returns:
        la page génerée par le template itineraires
    """
    itineraires = get_list_or_404(Itineraire)
    return render(request, 'itineraires/itineraires.html', {'itineraires': itineraires})


def sorties(request, itineraire_id):
    """
    Vue sur le detail d'un itineraire à visualiser:
    
    Args:
        request: la requête demandée
        itineraire_id: l'ID de l'itineraire selectionné en détail
        
    Returns:
        la page génerée par le template sorties
    """
    sorties = Sortie.objects.filter(itineraire_id=itineraire_id)
    itineraire_detail = get_object_or_404(Itineraire, pk=itineraire_id)
    return render(request, 'itineraires/sorties.html', {'sorties': sorties, 'itineraire_detail': itineraire_detail})


def sortie(request, user_id):
    """
    Vue sur le detail d'une sortie d'un utilisateur:
    
    Args:
        request: la requête demandée
        user_id: l'ID de l'utilisateur associé à la sortie
        
    Returns:
        la page génerée par le template sortie_detail
    """
    sortie = get_object_or_404(Sortie, pk=user_id)
    return render(request, 'itineraires/sortie_detail.html', {'sortie': sortie})

@login_required()
def nouvelle_sortie(request, itineraire_id):
    """
    Création d'une nouvelle sortie basée sur le modèle des sorties:
    
    Args:
        request: la requête demandée, GET ou POST
        
    Returns:
        - une page avec un formulaire vide si c'est une requête GET,
        - une page avec un formulaire vide si c'est une requête POST avec des champs invalides,
        - ou le detail de la sortie qui vient d'être modifié si c'est une requête POST avec des champs valides
    """
    if request.method == 'GET':
        form = SortieForm()
    elif request.method == 'POST':
        form = SortieForm(request.POST)
        if form.is_valid():
            sortie = form.save(commit=False)
            sortie.user = request.user
            sortie.itineraire = get_object_or_404(Itineraire, pk=itineraire_id)
            sortie.save()
            return redirect('itineraires:sortie', sortie.id)
    itineraire = get_object_or_404(Itineraire, pk=itineraire_id)
    return render(request,'itineraires/nouvelle_sortie.html', {'form': form, 'itineraire': itineraire})

@login_required()
def modif_sortie(request, user_id):
    """
    Modification d'une sortie existante basée sur le modèle des sorties:
    
    Args:
        request: la requête demandée, GET or POST
        user_id: l'ID de l'utilisateur associé à la sortie
        
    Returns:
        - une page avec un formulaire pré-rempli si c'est une requête GET,
        - une page avec un formulaire pré-rempli si c'est une requête POST avec des champs invalides,
        - ou le detail de la sortie qui vient d'être modifié si c'est une requête POST avec des champs valides
    """
    sortie = Sortie.objects.get(pk=user_id)
    if not (request.user.is_superuser) and (sortie.user != request.user):
        return HttpResponse("Vous ne pouvez modifier que les sorties dont vous n'êtes pas l'auteur.")
    elif request.method == 'GET':
        form = SortieForm(instance=sortie)
    elif request.method == 'POST':
        form = SortieForm(request.POST, instance=sortie)
        if form.is_valid():
            form.save()
            return redirect('itineraires:sortie', user_id=user_id)
    return render(request, 'itineraires/modif_sortie.html', {'form': form, 'sortie': sortie})
