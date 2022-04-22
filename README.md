# topoguide-julien-berndt

# Description

Nous allons réaliser une application itineraires pour le site topoguide. Le site codé sur django et dont on peut récuperer une base de donnée des utilisateurs/administrateurs existants va nous faciliter la tâche pour la partie authentification. Le seul aspect de l'authentification que nous aurons à génerer sera l'aspect de login/logout du site. Sur l'application itineraires, nous devront coder des vues qui nous permetrons de visualier la liste des itinéraires, la liste des sorties associés à cet itineraire, la sortie associée à un utilisateur ainsi que les fonctionalités de modification et d'ajout des sorties pour les utilisateurs connectés.

# Objectifs

1.Une page d'authentification
2.Une page de visualisation des itineraires avec la liste des itineraires proposés
3.Une page de visualisation des sorties avec la liste des sorties associés avec les itineraires et leur détail
4.Une page de visualisation d'une sortie dans son détail associé à un utilisateur
5.Une page de création de sortie pour un utilisateur et un itineraire
6.Une page de modification de sortie uniquement pour l'utilisateur de la sortie et les administrateurs
7.Une navigation entre les pages simplifiée

# Modèle itineraire

Le modèle itineraire est composé des champs suivants : 
    - le nom de l'itineraire
    - le point de départ
    - la description de l'itineraire
    - l'altitude de départ
    - l'altitude minimale
    - l'altitude maximale
    - le dénivelé positif cumulé
    - le dénivelé négatif cumulé
    - la durée estimée (en heures)
    - la difficulté estimée (de 1 à 5)

# Modèle itineraire

Le modèle sortie est composé des champs suivants :
    - l'utilisateur qui a enregistré la sortie
    - l'itinéraire correspondant
    - la date de la sortie
    - la durée réelle (en heures)
    - le nombre de personnes ayant participé à la sortie
    - l'expérience du groupe (à choisir dans une liste tous débutants, tous expérimentés, mixte)
    - la météo (à choisir dans une liste bonne, moyenne, mauvaise)
    - la difficulté ressentie (de 1 à 5)

# Navigation

Les options de navigation entre les vues sont les suivantes : 
    - Une navbar présente sur toute les vue sur le haut de la page qui possède des liens qui renvoient à la vue précedente (sauf pour la page de création qui possède un lien qui renvoie uniquement vers la liste des itineraires)
    - Dans la navbar est implémenté le nom de la session ouverte si un utilisateur est connecté ainsi qu'un bouton de connection/déconnection
    - Un bouton 'Detail' dans la liste des itineraires pour visualiser le détail d'un itineraire
    - Des boutons 'Consulter', 'Modifier', 'Nouvelle sortie' dans la liste des sorties pour respectivement visualiser le détail d'une sortie, accéder à la modification d'une sortie, accéder à la création d'une sortie
    - Des boutons 'Enregister' et 'Annuler' qui permettent d'accéder au détail de la sortie en cas d'enregistrement et de revenir à la page de détail de l'itineraire en cas d'annulation (sauf pour la page de création dont les boutons renvoient directement vers la liste des itineraires)

# Problèmes rencontrés et améliorations à apporter

Le fait que nous ne pouvont pas revenir en arrière à partir de la page de modification et que les boutons 'Enregistrer' et 'Annuler' ne renvoie pas à l'endroit où l'on veut qu'ils renvoient est un léger problème que je n'ai pas su résoudre.

De même pour la création d'une sortie permet à un utilisateur de pouvoir créer une sortie à partir de n'importe quel utilisateur et n'importe quel itineraire.

Comme pistes d'améliorations, je pensais à intégrer un bouton 'Supprimer' pour supprimer une sortie uniquement pour l'administrateur et les administrateurs. On pourrait aussi intégrer une page pour créer un itineraire à partir de la page de liste des itineraires. On pourrait aussi créer une barre de recherche pour les itineraires et rajouter des champs (Locatisation). On pourrais aussi, sur la page d'authentification, rajouter un lien pour rediriger vers une page de création de compte. Dans le menu, on pourrait rajouter une fonctionnalité de 'Paramètres' qui permettrait à l'utilisateur de modifier ses champs (mot de passe, nom, prénom, adresse mail, etc).