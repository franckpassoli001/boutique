from django.urls import path
from . import views

from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.db.models import Sum
from .models import Produit, Vente, Categorie
from .forms import ProduitForm, VenteForm, CategorieForm

def accueil(request):
    return render(request, 'gestion/index.html')

# 📌 Liste des produits
def liste_produits(request):
    produits = Produit.objects.all()
    return render(request, 'gestion/liste_produits.html', {'produits': produits})

# 📌 Ajouter un produit
def ajouter_produit(request):
    if request.method == "POST":
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_produits')
    else:
        form = ProduitForm()
    return render(request, 'gestion/ajouter_produit.html', {'form': form})

# 📌 Liste des ventes
def liste_ventes(request):
    ventes = Vente.objects.all().order_by('-date_vente')
    return render(request, 'gestion/liste_ventes.html', {'ventes': ventes})

# 📌 Ajouter une vente
def ajouter_vente(request):
    if request.method == "POST":
        form = VenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_ventes')
    else:
        form = VenteForm()
    return render(request, 'gestion/ajouter_vente.html', {'form': form})

# 📌 Tableau de bord
def tableau_de_bord(request):
    total_ventes = Vente.objects.aggregate(Sum('prix_total'))['prix_total__sum'] or 0
    total_produits = Produit.objects.aggregate(Sum('stock'))['stock__sum'] or 0
    return render(request, 'gestion/dashboard.html', {
        'total_ventes': total_ventes,
        'total_produits': total_produits
    })

# 📌 Liste des catégories
def liste_categories(request):
    categories = Categorie.objects.all()
    return render(request, 'gestion/liste_categories.html', {'categories': categories})

# 📌 Ajouter une catégorie
def ajouter_categorie(request):
    if request.method == 'POST':
        form = CategorieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_categories')
    else:
        form = CategorieForm()
    return render(request, 'gestion/ajouter_categorie.html', {'form': form})

def modifier_produit(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)
    if request.method == 'POST':
        form = ProduitForm(request.POST, instance=produit)
        if form.is_valid():
            form.save()
            return redirect('liste_produits')
    else:
        form = ProduitForm(instance=produit)
    return render(request, 'gestion/modifier_produit.html', {'form': form, 'produit': produit})

def supprimer_produit(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)
    produit.delete()
    return redirect('liste_produits')

def modifier_vente(request, vente_id):
    vente = get_object_or_404(Vente, id=vente_id)
    if request.method == "POST":
        form = VenteForm(request.POST, instance=vente)
        if form.is_valid():
            form.save()
            return redirect('liste_ventes')  # Redirige vers la liste des ventes
    else:
        form = VenteForm(instance=vente)

    return render(request, 'gestion/modifier_vente.html', {'form': form, 'vente': vente})

def supprimer_vente(request, vente_id):
    vente = get_object_or_404(Vente, id=vente_id)
    vente.delete()
    return redirect('liste_ventes')

def modifier_categorie(request, categorie_id):
    categorie = get_object_or_404(Categorie, id=categorie_id)
    if request.method == 'POST':
        form = CategorieForm(request.POST, instance=categorie)
        if form.is_valid():
            form.save()
            return redirect('liste_categories')
    else:
        form = CategorieForm(instance=categorie)
    return render(request, 'gestion/modifier_categorie.html', {'form': form, 'categorie': categorie})

def supprimer_categorie(request, categorie_id):
    categorie = get_object_or_404(Categorie, id=categorie_id)
    categorie.delete()
    return redirect('liste_categories')


