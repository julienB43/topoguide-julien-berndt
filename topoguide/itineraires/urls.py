from django.urls import path
from . import views

app_name = 'itineraires'
urlpatterns = [
    path('', views.itineraire, name='itineraire'),
    path('sorties/<int:itineraire_id>', views.sorties, name='sorties'),
    path('sortie/<int:user_id>', views.sortie, name='sortie'),
    path('nouvelle_sortie', views.nouvelle_sortie, name='nouvelle_sortie'),
    path('modif_sortie/<int:user_id>', views.modif_sortie, name='modif_sortie'),
]