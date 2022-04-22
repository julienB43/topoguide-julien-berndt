from django.db import models
from django.contrib.auth.models import User

class Itineraire(models.Model):
    """
    Un itineraire, avec plusieurs sorties associées
    """
    title = models.CharField('Nom', max_length=200)
    start = models.CharField('Point de départ', max_length=200)
    description = models.CharField('Description', max_length=1000)
    start_alt = models.IntegerField('Altitude de départ (m)')
    alt_min = models.IntegerField('Altitude minimale (m)')
    alt_max = models.IntegerField('Altitude maximale (m)')
    deniv_pos_cumul = models.IntegerField('Dénivelé positif cumulé (m)')
    deniv_neg_cumul = models.IntegerField('Dénivelé négatif cumulé (m)')
    duration = models.IntegerField('Durée (h)')
    difficulty = models.IntegerField('Difficulté (1-5)', choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    
    def __str__(self):
        """
        Nom générique de l'itineraire dans la base de donnée:
    
        Args:
            self: l'objet manipulé
        
        Returns:
            le nom de l'itineraire
        """
        return self.title
    
    def hour_as_min(self):
        """
        Durée en heures et en minutes pour ne pas se retrouver avec une durée en heure décimale:
    
        Args:
            self: l'objet manipulé
        
        Returns:
            - la durée en heures (au singulier ou au pluriel) si celle ci est uniquement en heures entières
            - le durée en minutes(au singulier ou au pluriel) si celle ci est inférieure à 1h
            - ou la durée en h et min si celle ci n'est pas en heures entières et est supérieur à 1h
        """
        hour = self.duration//1
        mins = (self.duration%1)*60
        if mins == 0:
            if hour == 1:
                return f'%d heure' % (hour)
            return f'%d heures' % (hour)
        if hour == 0:
            if mins == 1:
                return f'%d minute' % (mins)
            return f'%d minutes' % (mins)
        return f'%dh %dmin' % (hour,mins)
    
class Sortie(models.Model):
    """
    Une sortie pour un itineraire et un utilisateur donnés
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    itineraire = models.ForeignKey(Itineraire, on_delete=models.CASCADE)
    
    date_sortie = models.DateTimeField('Date de la sortie')
    real_duration = models.IntegerField('Durée réelle (h)')
    nb_people = models.IntegerField('Nombre de participants')
    exp_grp = models.CharField('Type de randonneur', choices=[('tous_débutants', 'Tous débutants'), ('tous_expérimentés','Tous expérimentés'), ('mixte', 'Mixte')], max_length=20)
    weather = models.CharField('Météo', choices=[('bonne', 'Bonne'), ('moyenne', 'Moyenne'), ('mauvaise', 'Mauvaise')], max_length=10)
    difficulty_felt = models.IntegerField('Difficulté (1-5)', choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    
    def __str__(self):
        """
        Nom générique de la sortie dans la base de donnée:
    
        Args:
            self: l'objet manipulé
        
        Returns:
            le nom
        """
        return 'Sortie à ' + self.itineraire.title + ' de ' + self.user.username
    
    def hour_as_min(self):
        """
        Durée en heures et en minutes pour ne pas se retrouver avec une durée en heure décimale:
    
        Args:
            self: l'objet manipulé
        
        Returns:
            - la durée en heures (au singulier ou au pluriel) si celle ci est uniquement en heures entières
            - le durée en minutes(au singulier ou au pluriel) si celle ci est inférieure à 1h
            - ou la durée en h et min si celle ci n'est pas en heures entières et est supérieur à 1h
        """
        hour = self.real_duration//1
        mins = (self.real_duration%1)*60
        if mins == 0:
            if hour == 1:
                return f'%d heure' % (hour)
            return f'%d heures' % (hour)
        if hour == 0:
            if mins == 1:
                return f'%d minute' % (mins)
            return f'%d minutes' % (mins)
        return f'%dh %dmin' % (hour,mins)