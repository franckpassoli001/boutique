from django import forms
from .models import Produit, Vente, Categorie

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['nom', 'categorie', 'prix', 'stock']

class VenteForm(forms.ModelForm):
    class Meta:
        model = Vente
        fields = ['produit', 'quantite']

class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['nom']
