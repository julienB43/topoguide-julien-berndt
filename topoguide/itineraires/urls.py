from django.urls import path
from . import views

app_name = 'itineraires'
urlpatterns = [
    path('sortie/<int:user_id>', views.sortie, name='sortie'),
    path('', views.itineraire, name='itineraire'),
    path('sorties/<int:itineraire_id>', views.sorties, name='sortie')
]