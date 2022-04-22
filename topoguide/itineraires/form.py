from django import forms

from .models import Sortie

class SortieModifForm(forms.ModelForm):
    class Meta:
        model = Sortie
        fields = '__all__' # ['date_sortie', 'real_duration','nb_people', 'exp_grp', 'weather', 'difficulty_felt']
        exclude = ('user', 'itineraire')
        
class SortieForm(forms.ModelForm):
    class Meta:
        model = Sortie
        fields = '__all__'