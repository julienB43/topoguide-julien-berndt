from django import forms

from .models import Sortie

class SortieModifForm(forms.ModelForm):
    class Meta:
        model = Sortie
        fields = '__all__'
        exclude = ('user', 'itineraire')
        
class SortieForm(forms.ModelForm):
    class Meta:
        model = Sortie
        fields = '__all__'