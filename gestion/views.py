from os import path

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from .models import Locataire
from .models import Appartement, AffectationAppartement, EtatDesLieux, Paiement, QuittanceLoyer
from django.http import HttpResponseNotAllowed


# Create your views here.


def index(request):
    return render(request,'index.html')



def appartement_list(request):
    if request.method == 'POST':
        appartements = Appartement.objects.all()
        return render(request, 'appartement_list.html', {'appartements': appartements} )
    else:
        return HttpResponseNotAllowed(['POST'])


def locataire_list(request):
    if request.method == 'POST':
        locataires = Locataire.objects.all()
        return render(request, 'locataire_list.html', {'locataires': locataires}
                      )
    else:
        return HttpResponseNotAllowed(['POST'])


def affectation_appartement_list(request):
    if request.method == 'POST':
        affectation_appartements = AffectationAppartement.objects.all()
        return render(request, 'affectation_appartement_list.html', {'affectation_appartements': affectation_appartements} )
    else:
        return HttpResponseNotAllowed(['POST'])


def etat_des_lieux_list(request):
    if request.method == 'POST':
        etat_des_lieux = EtatDesLieux.objects.all()
        return render(request, 'etat_des_lieux_list.html', {'etat_des_lieux': etat_des_lieux} )
    else:
        return HttpResponseNotAllowed(['POST'])


def paiement_list(request):
    if request.method == 'POST':
        paiements = Paiement.objects.all()
        return render(request, 'paiement_list.html', {'paiements': paiements} )
    else:
        return HttpResponseNotAllowed(['POST'])


def quittance_loyer_list(request):
    if request.method == 'POST':
        quittance_loyers = QuittanceLoyer.objects.all()
        return render(request, 'quittance_loyer_list.html', {'quittance_loyers': quittance_loyers} )
    else:
        return HttpResponseNotAllowed(['POST'])




