from django.test import TestCase
from .models import Locataire, Appartement, AffectationAppartement
from datetime import date
from django.utils import timezone


class LocataireTest(TestCase):
    def setUp(self):
        self.locataire = Locataire.objects.create(nom="Dupont", adresse="1 rue de la Paix", numero_telephone="0123456789", adresse_email="dupont@example.com")

    def test_str(self):
        self.assertEqual(str(self.locataire), "Dupont")



class AppartementTest(TestCase):
    def test_creation_appartement(self):
        # Vérifier qu'il n'y a pas d'appartement avant la création
        self.assertEqual(Appartement.objects.count(), 0)

        # Créer un locataire pour l'associer à l'appartement
        locataire = Locataire.objects.create(nom="Dupont", adresse="1 rue de la Paix", numero_telephone="0123456789",
                                             adresse_email="dupont@example.com")

        # Créer un appartement
        appartement = Appartement.objects.create(adresse="2 rue de la Liberté", complement_adresse="Appartement 3",
                                                 ville="Paris", code_postal="75001", prix_charges=1000.00,
                                                 loyer=1500.00, depot_garantie=3000.00, locataire=locataire)

        # Vérifier qu'il y a maintenant un appartement en base de données
        self.assertEqual(Appartement.objects.count(), 1)

        # Vérifier que l'adresse de l'appartement a bien été sauvegardée
        self.assertEqual(appartement.adresse, "2 rue de la Liberté")

        # Vérifier que le locataire associé à l'appartement est bien celui créé précédemment
        self.assertEqual(appartement.locataire, locataire)

class AffectationAppartementTest(TestCase):

    def setUp(self):
        self.locataire = Locataire.objects.create(nom="Dupont", adresse="1 rue de la Paix",
                                                  numero_telephone="0123456789", adresse_email="dupont@example.com")
        self.appartement = Appartement.objects.create(adresse="1 rue de la Paix", complement_adresse="", ville="Paris",
                                                      code_postal="75001", prix_charges=50, loyer=1000,
                                                      depot_garantie=2000, locataire=None)
        self.date_debut = date.today()
        self.date_fin = self.date_debut.replace(year=self.date_debut.year + 1)

    def test_affectation_appartement_creation(self):
        affectation = AffectationAppartement.objects.create(appartement=self.appartement, locataire=self.locataire,
                                                            date_debut=self.date_debut, date_fin=self.date_fin)
        self.assertEqual(affectation.appartement, self.appartement)
        self.assertEqual(affectation.locataire, self.locataire)
        self.assertEqual(affectation.date_debut, self.date_debut)
        self.assertEqual(affectation.date_fin, self.date_fin)

    def test_affectation_appartement_str(self):
        affectation = AffectationAppartement.objects.create(appartement=self.appartement, locataire=self.locataire,
                                                            date_debut=self.date_debut, date_fin=self.date_fin)
        self.assertEqual(str(affectation), f"{self.locataire.nom} - {self.appartement.adresse}")

