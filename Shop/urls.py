from django.urls import path
from . import views

urlpatterns = [
    path('Shop/', views.Accueil, name='Shop'),
    path('AchatDetail/<ProduitName>', views.AchatDetail, name='detail'),
    path('Delete/<ProduitName>', views.Delete, name='delete'),
    path('Modif/<ProduitName>', views.Modif, name='Modif'),
    path('ModifDone/', views.ModifDone, name='ModifDone'), 
    path('produitAjoute/', views.produitAjoute, name='produitAjoute'),
    path('Ajout/', views.Ajout, name='Ajout'),
    path('panier/', views.Panier, name='detail'),

]
