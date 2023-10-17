from django.urls import path
from . import views

urlpatterns = [
    path('Shop/', views.Accueil, name='Shop'),
    path('AchatDetail/<ProduitName>', views.AchatDetail, name='detail'),
    path('ModifPanier/<ProduitName>&<PanierProduitId>', views.ModifPanier, name='ModifPanier'),
    path('panier/', views.Panier, name='ListPanier'),
    path('DeletePanier/<PanierProduitId>', views.DeletePanier, name='deletePanier'),

    

]
