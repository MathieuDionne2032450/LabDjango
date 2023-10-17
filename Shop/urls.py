from django.urls import path
from . import views

urlpatterns = [
    path('Shop/', views.Accueil, name='Shop'),
    path('AchatDetail/<ProduitName>', views.AchatDetail, name='detail'),
    path('panier', views.AchatDetail, name='detail'),

]
