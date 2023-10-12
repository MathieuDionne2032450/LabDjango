from django.urls import path
from . import views

urlpatterns = [
    path('Shop/', views.Accueil, name='Shop'),
]
