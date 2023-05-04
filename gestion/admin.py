from django.contrib import admin
from .models import Appartement
from .models import Locataire
from .models import EtatDesLieux
from .models import Paiement
from .models import QuittanceLoyer
from .models import AffectationAppartement

class LocataireAdmin(admin.ModelAdmin):
    list_display = ('nom', 'adresse', 'numero_telephone', 'adresse_email')
    search_fields = ['nom']

class AppartementAdmin(admin.ModelAdmin):
    list_display = ( 'adresse', 'complement_adresse', 'ville', 'code_postal', 'prix_charges', 'loyer', 'depot_garantie')
    search_fields = ['adresse']

class EtatDesLieuxAdmin(admin.ModelAdmin):
    list_display = ('appartement', 'date', 'remarques')
    search_fields = ['date']

class PaiementAdmin(admin.ModelAdmin):
    list_display = ('locataire','date', 'montant')
    search_fields = ['date']

class QuittanceLoyerAdmin(admin.ModelAdmin):
    list_display = ( 'locataire', 'periode', 'montant')
    search_fields = ['periode']

class AffectationAppartementAdmin(admin.ModelAdmin):
    list_display = ( 'appartement', 'locataire', 'date_debut', 'date_fin')
    search_fields = ['locataire']



# Register your models here
admin.site.register(Appartement, AppartementAdmin)
admin.site.register(Locataire, LocataireAdmin)
admin.site.register(EtatDesLieux, EtatDesLieuxAdmin)
admin.site.register(Paiement, PaiementAdmin)
admin.site.register(QuittanceLoyer, QuittanceLoyerAdmin)
admin.site.register(AffectationAppartement, AffectationAppartementAdmin)