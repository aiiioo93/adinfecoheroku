from django.contrib import admin
from django.urls import path
from . import views

from django.urls import reverse




urlpatterns = [
    path('', views.index, name="index"),
    path('appartement_list', views.appartement_list, name='appartement_list'),
    path('locataire_list', views.locataire_list, name='locataire_list'),
    path('affectation_appartement_list', views.affectation_appartement_list, name='affectation_appartement_list'),
    path('etat_des_lieux_list', views.etat_des_lieux_list, name='etat_des_lieux_list'),
    path('paiement_list', views.paiement_list, name='paiement_list'),
    path('quittance_loyer_list', views.quittance_loyer_list, name='quittance_loyer_list'),



]
