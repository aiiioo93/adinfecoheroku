from django.core.exceptions import ValidationError
from django.db.models import Q
from django.db import models
from django.utils.translation import gettext_lazy as _


class Locataire(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    numero_telephone = models.CharField(max_length=20)
    adresse_email = models.EmailField(max_length=254)


    def __str__(self):
        return f"{self.nom}  {self.prenom}"


class Appartement(models.Model):
    adresse = models.CharField(max_length=200)
    ville = models.CharField(max_length=50)
    code_postal = models.CharField(max_length=10)
    prix_charges = models.DecimalField(max_digits=10, decimal_places=2)
    loyer = models.DecimalField(max_digits=10, decimal_places=2)
    depot_garantie = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.adresse


class AffectationAppartement(models.Model):
    appartement = models.OneToOneField(Appartement, on_delete=models.CASCADE)
    locataire = models.OneToOneField(Locataire, on_delete=models.CASCADE)
    date_debut = models.DateField()
    date_fin = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.locataire.nom} {self.locataire.prenom} -  {self.appartement.adresse}"

class EtatDesLieux(models.Model):
    appartement = models.ForeignKey(Appartement, on_delete=models.CASCADE)
    date = models.DateField()
    remarques = models.TextField()

    def __str__(self):
        return f"{self.appartement.adresse} - {self.date}"


class Paiement(models.Model):
    appartement = models.ForeignKey(AffectationAppartement, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField()
    montant = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f" {self.date.strftime('%Y-%m-%d')} - {self.montant:.2f}"


class QuittanceLoyer(models.Model):
    locataire = models.ForeignKey(Locataire, on_delete=models.CASCADE)
    periode = models.DateField()
    montant = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f"{self.locataire.nom} - {self.periode.strftime('%B %Y')}"
