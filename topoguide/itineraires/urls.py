from django.urls import path
from . import views

app_name = 'itineraires'
urlpatterns = [
    path('', views.itineraire),
]