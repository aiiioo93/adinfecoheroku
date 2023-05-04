from django.test import TestCase
from .models import Locataire

class LocataireTest(TestCase):
    def setUp(self):
        self.locataire = Locataire.objects.create(nom="Dupont", adresse="1 rue de la Paix", numero_telephone="0123456789", adresse_email="dupont@example.com")

    def test_str(self):
        self.assertEqual(str(self.locataire), "Dupont")
