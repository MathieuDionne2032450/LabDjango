from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from . import models



def Accueil(request):
    produits = models.Produit.objects.all()
    
    context = {
        'prod_list': produits,
    }
    return render(request,'Accueil.html',context)

#Affiche la page pour choisir les détails de l'objet acheté
def AchatDetail(request,ProduitName):
    produit = models.Produit.objects.all().filter(name=ProduitName).values()[0]
    quantite = 1
    niveau = 1
    chemin = "Chemin 1"
    panierId = 0
    context = {
        'quantite':quantite,
        'Niveau':niveau,
        'Chemin':chemin,
        'produit': produit,
        'panierId':panierId,
    }
    return render(request,'AchatDetail.html',context)

#La page est la même que celle d'AchatDetail sauf quel reçoit d'autre variable en parametre pour permettre de remplire les input d'avance
def ModifPanier(request,ProduitName,PanierProduitId):
    
    produit = models.Produit.objects.all().filter(name=ProduitName).values()[0]
    PanierProduit = models.PanierProduit.objects.all().filter(id = PanierProduitId).values()[0]

    quantite = 1
    niveau = 1
    chemin = "Chemin 1"
    panierId = 0

    if(PanierProduit != None):
        quantite = PanierProduit.get("quantite")
        niveau = PanierProduit.get("ameliorationNiveau")
        chemin = PanierProduit.get("ameliorationChemin")
        panierId = PanierProduit.get("id")
    
    context = {
        'quantite':quantite,
        'Niveau':niveau,
        'Chemin':chemin,
        'panierId':panierId,
        'produit': produit,

    }
    return render(request,'AchatDetail.html',context)

#Cette page s'occupe de créer ou modifier de produit dans le panier
def Panier(request):

    if(request.method == 'POST'):
        if(request.POST["panierId"] == 0):
            hist1 = models.PanierProduit(nomProduit=request.POST["nomProduit"],quantite=request.POST["quantite"],ameliorationChemin = request.POST["Amelioration"],ameliorationNiveau = request.POST["NumeroEvolution"])
            hist1.save()

            
     
    panierList = models.PanierProduit.objects.all()

    context = {
        'panier_liste': panierList
    }
    return render(request,'panier.html',context)

def DeletePanier(request,PanierProduitId):
    models.PanierProduit.objects.all().filter(id = PanierProduitId).delete()

    historique = models.PanierProduit.objects.all()

    context = {
        'panier_liste': historique
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
    