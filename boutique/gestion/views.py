from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import Produit, Vente
from .forms import ProduitForm, VenteForm

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
from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import Produit, Vente
from .forms import ProduitForm, VenteForm

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
from django.shortcuts import render

def accueil(request):
    return render(request, 'gestion/index.html')
