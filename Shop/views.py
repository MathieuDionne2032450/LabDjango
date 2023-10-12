from django.shortcuts import render
from django.template import loader
from . import models

def Accueil(request):
    produits = models.Produit.objects.all()
    
    context = {
        'prod_list': produits,
    }
    return render(request,'Accueil.html',context)

def AchatDetail(request,ProduitName):
   
    produit = models.Produit.objects.all().filter(name=ProduitName).values()[0]
    context = {
        'ProduitName':ProduitName,
        'produit': produit,
    }
    return render(request,'AchatDetail.html',context)