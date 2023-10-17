from django.db import models

# Create your models here.
from django.db import models

class Produit(models.Model):
    name = models.CharField(max_length=255)
    Description = models.CharField(max_length=255)
    prix = models.BigIntegerField()
    img = models.CharField(max_length=255)

class PanierProduit(models.Model):
    nomProduit = models.CharField(max_length=255)
    quantite = models.IntegerField(max_length=255)
    ameliorationChemin = models.CharField(max_length=255)
    ameliorationNiveau = models.IntegerField(max_length=255)