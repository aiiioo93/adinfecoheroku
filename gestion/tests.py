from django.test import TestCase
from .models import Locataire, Appartement

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
