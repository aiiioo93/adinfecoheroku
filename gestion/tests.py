from django.test import TestCase
from .models import Locataire, Appartement, AffectationAppartement, EtatDesLieux
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

        from datetime import date
        from django.test import TestCase
        from gestion.models import Appartement, EtatDesLieux

class EtatDesLieuxTest(TestCase):
    def setUp(self):
        # Création d'un objet Appartement pour les tests
        self.appartement = Appartement.objects.create(
            adresse="1 rue de la Paix",
            complement_adresse="",
            ville="Paris",
            code_postal="75000",
            prix_charges=100.00,
            loyer=500.00,
            depot_garantie=500.00
        )

        # Création d'un objet EtatDesLieux pour les tests
        self.date = date.today()
        self.remarques = "Appartement en bon état"
        self.etat_des_lieux = EtatDesLieux.objects.create(
            appartement=self.appartement,
            date=self.date,
            remarques=self.remarques
        )

    def test_etat_des_lieux_creation(self):
        # Vérifie si l'objet EtatDesLieux a été créé avec les valeurs attendues
        self.assertEqual(self.etat_des_lieux.appartement, self.appartement)
        self.assertEqual(self.etat_des_lieux.date, self.date)
        self.assertEqual(self.etat_des_lieux.remarques, self.remarques)

    def test_etat_des_lieux_str(self):
        # Vérifie si la méthode __str__ de l'objet EtatDesLieux renvoie la valeur attendue
        expected_output = f"{self.appartement} - {self.date}"
        self.assertEqual(str(self.etat_des_lieux), expected_output)

    def test_etat_des_lieux_date_non_nulle(self):
        # Vérifie que la date de l'objet EtatDesLieux n'est pas nulle
        self.assertIsNotNone(self.etat_des_lieux.date)

    def test_etat_des_lieux_remarques_non_nulles(self):
        # Vérifie que les remarques de l'objet EtatDesLieux ne sont pas nulles
        self.assertIsNotNone(self.etat_des_lieux.remarques)


