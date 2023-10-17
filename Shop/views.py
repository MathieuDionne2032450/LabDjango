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

def Panier(request):

    historique = models.PanierProduit.objects.all()

    hist1 = models.PanierProduit(nomProduit="test",quantite=0,ameliorationChemin = "Chemin 1",ameliorationNiveau = 1)
    hist1.save()

    context = {
        'historique_liste': historique
    }
    return render(request,'panier.html',context)

def Modif(request,ProduitName):
    produit = models.Produit.objects.all().filter(name=ProduitName).values()[0]
    context = {
        'produit': produit,
    }
    return render(request,'Modif.html',context)


def Delete(request,ProduitName):
    models.Produit.objects.all().filter(name=ProduitName).delete()
    
    

    produits = models.Produit.objects.all()
    context = {
        'prod_list': produits,
    }
    return render(request,'Accueil.html',context)

def Ajout(request):
    produits = models.Produit.objects.all()
    context = {
        'prod_list': produits,
    }
    return render(request,'Ajout.html',context)

def ModifDone(request):
    OldName = request.POST['oldname']
    NewName = request.POST['newname']
    Prix = request.POST['prix']
    Desc = request.POST['desc']

    models.Produit.objects.all().filter(name=OldName).update(name=NewName)
    models.Produit.objects.all().filter(name=OldName).update(prix=Prix)
    models.Produit.objects.all().filter(name=OldName).update(Description=Desc)

    produits = models.Produit.objects.all()
    context = {
        'prod_list': produits,
    }
    return render(request,'Accueil.html',context)
    
def produitAjoute(request):
    Name = request.POST['name']
    Prix = request.POST['prix']
    Desc = request.POST['desc']

    prod1 = models.Produit(name=Name,Description=Desc,prix=Prix,img="base.jpg")
    prod1.save()

    produits = models.Produit.objects.all()
    context = {
        'prod_list': produits,
    }
    return render(request,'Accueil.html',context)
    