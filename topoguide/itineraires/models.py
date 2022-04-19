from django.db import models
from django.contrib.auth.models import User

class Itineraire(models.Model):
    
    title = models.CharField('Nom', max_length=200)
    start = models.CharField('Point de départ', max_length=200)
    description = models.CharField('Description', max_length=1000)
    start_alt = models.IntegerField('Altitude de départ (m)')
    alt_min = models.IntegerField('Altitude minimale (m)')
    alt_max = models.IntegerField('Altitude maximale (m)')
    deniv_pos_cumul = models.IntegerField('Dénivelé positif cumulé (m)')
    deniv_neg_cumul = models.IntegerField('Dénivelé négatif cumulé (m)')
    duration = models.IntegerField('Durée (h)')
    difficulty = models.IntegerField('Difficulté (1-5)')
    
    def __self__(self):
        return self.nom
    
class Sortie(models.Model):
    
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    itineraire = models.ForeignKey('Itineraire', on_delete=models.CASCADE)
    
    date_sortie = models.DateTimeField('Date de la sortie')
    real_duration = models.IntegerField('Durée réelle (h)')
    nb_people = models.IntegerField('Nombre de participants')
    exp_grp = models.CharField(choices=[('tous_débutants', 'tous débutants'), ('tous_expérimentés','tous expérimentés'), ('mixte', 'mixte')], max_length=20)
    weather = models.CharField(choices=[('bonne', 'bonne'), ('moyenne', 'moyenne'), ('mauvaise', 'mauvaise')], max_length=10)
    difficulty_felt = models.IntegerField('Difficulté (1-5)')