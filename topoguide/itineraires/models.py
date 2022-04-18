from tkinter import CASCADE
from django.db import models

class Itineraires(models.Model):
    title = models.CharField(max_length=200)
    start = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    start_alt = models.IntegerField('Altitude de départ (m)')
    alt_min = models.IntegerField('Altitude minimale (m)')
    alt_max = models.IntegerField('Altitude maximale (m)')
    deniv_pos_cumul = models.IntegerField('Dénivelé positif cumulé (m)')
    deniv_neg_cumul = models.IntegerField('Dénivelé négatif cumulé (m)')
    
    duration = models.IntegerField('Durée (min)')
    dificulty = models.IntegerField('Dificulté (1-5)')
    
    def __self__(self):
        return self.title
