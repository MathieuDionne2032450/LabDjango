from django.shortcuts import render
from django.template import loader
from . import models



def Accueil(request):
    produits = models.Produit.objects.all()

    for p in produits:
        p.delete()


    prod1 = models.Produit(name="ace",Description="Des volées au-dessus des volées de fléchettes au sol.",prix=680,img="ace.png")
    prod1.save()
    prod1 = models.Produit(name="alchimiste",Description="Exploiter les pouvoirs de la science et de la magie, éclabousse Bloons avec de l'acide, infuser diverses potions avec différents effets.",prix=470,img="alchimiste.png")
    prod1.save()
    prod1 = models.Produit(name="beast",Description="Les trains terrestres, l'eau ou les bêtes d'air. Les multiples Beast Handlers peuvent avoir leurs propres bêtes, ou combiner des efforts pour former une seule bête avec un plus grand pouvoir de bête.",prix=210,img="beast.png")
    prod1.save()
    prod1 = models.Produit(name="boomrang",Description="Hurls un boomerang qui suit un chemin courbe. Bonne portée et percer.",prix=275,img="boomrang.png")
    prod1.save()
    prod1 = models.Produit(name="cannon",Description="Lance une bombe puissante aux Bloons. Lenteur du tir mais affecte un rayon autour de l'explosion.",prix=445,img="cannon.png")
    prod1.save()
    prod1 = models.Produit(name="dart",Description="Jette une seule fléchette à Bloons. Courte portée et faible perce mais bon marché.",prix=170,img="dart.png")
    prod1.save()
    prod1 = models.Produit(name="dartling",Description="Utilise une machine de fléchettes. Vise où que vous ayez tapoté pour la dernière fois sur l'écran.",prix=720,img="dartling.png")
    prod1.save()
    prod1 = models.Produit(name="druid",Description="Crée une explosion d'épines pour chaque attaque. Les mises à niveau peuvent appeler les pouvoirs de la Jungle, de la Tempête ou de la Sortir.",prix=340,img="druid.png")
    prod1.save()
    prod1 = models.Produit(name="factory",Description="Générer automatiquement des piles de Road Spikes sur la voie voisine. Excellente dernière ligne de défense.",prix=850,img="factory.png")
    prod1.save()
    prod1 = models.Produit(name="farm",Description="Génère des bananes à chaque tour qui se transforment en argent de jeu pour dépenser pour plus de choses.",prix=1060,img="farm.png")
    prod1.save()
    prod1 = models.Produit(name="glue",Description="Tire sur un blob de colle collante qui ralentit Bloons de 50%.",prix=190,img="glue.png")
    prod1.save()
    prod1 = models.Produit(name="heli",Description="Hovers où que vous le dirigez. Des pousses de deux canons de fléchettes lourdes.",prix=1360,img="heli.png")
    prod1.save()
    prod1 = models.Produit(name="ice",Description="Pops et gèle à proximité Bloons pendant une courte période. Les Bloons congelés sont à l'abri des dommages aigus. Je ne peux pas congeler les blouses blanches, les zèbres ou les bloçons de plomb.",prix=450,img="ice.png")
    prod1.save()
    prod1 = models.Produit(name="ingenieur",Description="Prend un clou de confiance pour pop Bloons. Peut améliorer ses propres tourillons de senterie.",prix=340,img="ingenieur.png")
    prod1.save()
    prod1 = models.Produit(name="magic",Description="Hurls bolts magiques d'énergie aux Bloons. Peut passer à une variété de sorts puissants.",prix=320,img="magic.png")
    prod1.save()
    prod1 = models.Produit(name="mortier",Description="Lance un obus de mortier explosant vers un emplacement fixe n'importe où sur l'écran.",prix=640,img="mortier.png")
    prod1.save()
    prod1 = models.Produit(name="ninja",Description="Singe furtif et rapide qui jette des cris de brouillés à la pop the Bloons. Peut cibler Camo Bloons.",prix=425,img="ninja.png")
    prod1.save()
    prod1 = models.Produit(name="pirate",Description="Tire une seule fléchette lourde des deux côtés du navire. Doit être placé dans l'eau.",prix=425,img="pirate.png")
    prod1.save()
    prod1 = models.Produit(name="sniper",Description="Il peut tirer Bloons qu'il peut voir n'importe où sur l'écran avec un fusil à longue portée, et sape 2 couches de Bloons frappés par lui.",prix=300,img="sniper.png")
    prod1.save()
    prod1 = models.Produit(name="sousmarin",Description="Tire sur les torpes à proximité de Bloons. Doit être placé dans l'eau.",prix=275,img="sousmarin.png")
    prod1.save()
    prod1 = models.Produit(name="super",Description="Jette des centaines de fléchettes à vitesse hypersonique avec une énorme portée d'attaque.",prix=2125,img="super.png")
    prod1.save()
    prod1 = models.Produit(name="tack",Description="Il tire une volée à courte portée de tacks pointus dans 8 directions.",prix=240,img="tack.png")
    prod1.save()
    prod1 = models.Produit(name="village",Description="Hub of Monkey industry, a un certain nombre d'avantages différents pour aider tous vos singes. Augmente la gamme de tous les singes dans son rayon de 10 %.",prix=1020,img="village.png")
    prod1.save()
    
   
    
    

    context = {
        'prod_list': produits,
    }
    return render(request,'Accueil.html',context)

