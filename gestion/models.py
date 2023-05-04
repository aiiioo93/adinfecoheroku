from django.db import models

class Locataire(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=200)
    numero_telephone = models.CharField(max_length=20)
    adresse_email = models.EmailField(max_length=254)

    def __str__(self):
        return self.nom

