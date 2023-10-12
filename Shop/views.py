from django.shortcuts import render
from django.template import loader
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

