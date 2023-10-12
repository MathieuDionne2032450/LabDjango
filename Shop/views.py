from django.shortcuts import render
from django.template import loader
from . import models

def Accueil(request):
    produits = models.Produit.objects.all()
    context = {
        'name': 'test',
        'Description': '123',
        'prix' : '456',
        'img' : '789',
        'prod_list': produits,
    }
    return render(request,'Accueil.html',context)

