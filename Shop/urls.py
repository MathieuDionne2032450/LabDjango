from django.urls import path
from . import views

urlpatterns = [
    path('Shop/', views.Home, name='Shop'),
    path('AchatDetail/<ProduitName>', views.AchatDetail, name='detail'),
    path('ModifPanier/<ProduitName>&<PanierProduitId>', views.ModifPanier, name='ModifPanier'),
    path('panier/', views.Panier, name='ListPanier'),
    path('DeletePanier/<PanierProduitId>', views.DeletePanier, name='deletePanier'),
    path('Delete/<ProduitName>', views.Delete, name='delete'),
    path('Modif/<ProduitName>', views.Modif, name='Modif'),
    path('ModifDone/', views.ModifDone, name='ModifDone'), 
    path('produitAjoute/', views.produitAjoute, name='produitAjoute'),
    path('Ajout/', views.Ajout, name='Ajout'),
    path('Accueil/', views.Accueil, name='Accueil'),

]
