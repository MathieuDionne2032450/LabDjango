from django.shortcuts import render
from django.template import loader
from . import models

def Accueil(request):
    produits = models.Produit.objects.all()
    test = models.Produit(name="Poire",Description="432",prix = 5, img="fsdfr")
    test.save()
    context = {
        'prod_list': produits,
    }
    return render(request,'Accueil.html',context)

def AchatDetail(request,ProduitName):
    produit = models.Produit.objects.filter(name='name')
    context = {
        'produit': produit,
    }
    return render(request,'AchatDetail.html',context)