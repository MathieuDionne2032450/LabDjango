from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from . import models



def Accueil(request):
    produits = models.Produit.objects.all()

    for p in produits:
        p.delete()


    prod1 = models.Produit(name="ace",Description="avion",prix=350,img="ace.png")
    prod1.save()
    prod1 = models.Produit(name="alchimiste",Description="potions",prix=450,img="alchimiste.png")
    prod1.save()
    prod1 = models.Produit(name="beast",Description="beast handler",prix=850,img="beast.png")
    prod1.save()
    prod1 = models.Produit(name="boomrang",Description="lanceur de dart",prix=350,img="boomrang.png")
    prod1.save()
    prod1 = models.Produit(name="cannon",Description="lanceur de dart",prix=350,img="cannon.png")
    prod1.save()
    prod1 = models.Produit(name="dart",Description="avion",prix=350,img="dart.png")
    prod1.save()
    prod1 = models.Produit(name="dartling",Description="potions",prix=450,img="dartling.png")
    prod1.save()
    prod1 = models.Produit(name="druid",Description="beast handler",prix=850,img="druid.png")
    prod1.save()
    prod1 = models.Produit(name="factory",Description="lanceur de dart",prix=350,img="factory.png")
    prod1.save()
    prod1 = models.Produit(name="farm",Description="lanceur de dart",prix=350,img="farm.png")
    prod1.save()
    prod1 = models.Produit(name="glue",Description="avion",prix=350,img="glue.png")
    prod1.save()
    prod1 = models.Produit(name="heli",Description="potions",prix=450,img="heli.png")
    prod1.save()
    prod1 = models.Produit(name="ice",Description="beast handler",prix=850,img="ice.png")
    prod1.save()
    prod1 = models.Produit(name="ingenieur",Description="lanceur de dart",prix=350,img="ingenieur.png")
    prod1.save()
    prod1 = models.Produit(name="magic",Description="lanceur de dart",prix=350,img="magic.png")
    prod1.save()
    prod1 = models.Produit(name="mortier",Description="avion",prix=350,img="mortier.png")
    prod1.save()
    prod1 = models.Produit(name="ninja",Description="potions",prix=450,img="ninja.png")
    prod1.save()
    prod1 = models.Produit(name="pirate",Description="beast handler",prix=850,img="pirate.png")
    prod1.save()
    prod1 = models.Produit(name="sniper",Description="lanceur de dart",prix=350,img="sniper.png")
    prod1.save()
    prod1 = models.Produit(name="sousmarin",Description="lanceur de dart",prix=350,img="sousmarin.png")
    prod1.save()
    prod1 = models.Produit(name="super",Description="avion",prix=350,img="super.png")
    prod1.save()
    prod1 = models.Produit(name="tack",Description="potions",prix=450,img="tack.png")
    prod1.save()
    prod1 = models.Produit(name="village",Description="beast handler",prix=850,img="village.png")
    prod1.save()

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
    