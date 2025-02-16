from django.urls import path
from .views import liste_produits, ajouter_produit, liste_ventes, ajouter_vente, tableau_de_bord

urlpatterns = [
    path('', liste_produits, name='liste_produits'),
    path('ajouter/', ajouter_produit, name='ajouter_produit'),
    path('ventes/', liste_ventes, name='liste_ventes'),
    path('ventes/ajouter/', ajouter_vente, name='ajouter_vente'),
    path('dashboard/', tableau_de_bord, name='dashboard'),
]
from django.shortcuts import render

def accueil(request):
    return render(request, 'gestion/index.html')
