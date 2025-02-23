from django.contrib import admin
from django.urls import path
from gestion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.accueil, name='index'),  # ✅ Changer views.index en views.accueil
    path('produits/', views.liste_produits, name='liste_produits'),
    path('ventes/', views.liste_ventes, name='liste_ventes'),
    path('dashboard/', views.tableau_de_bord, name='dashboard'),
    path('categories/', views.liste_categories, name='liste_categories'),
    path('produit/ajouter/', views.ajouter_produit, name='ajouter_produit'),
    path('vente/ajouter/', views.ajouter_vente, name='ajouter_vente'),
    path('categorie/ajouter/', views.ajouter_categorie, name='ajouter_categorie'),
    path('produit/modifier/<int:produit_id>/', views.modifier_produit, name='modifier_produit'),
    path('produit/supprimer/<int:produit_id>/', views.supprimer_produit, name='supprimer_produit'),
    path('ventes/', views.liste_ventes, name='liste_ventes'),
    path('ventes/ajouter/', views.ajouter_vente, name='ajouter_vente'),
    path('ventes/modifier/<int:vente_id>/', views.modifier_vente, name='modifier_vente'),
    path('ventes/supprimer/<int:vente_id>/', views.supprimer_vente, name='supprimer_vente'),
    path('categories/', views.liste_categories, name='liste_categories'),
    path('categories/ajouter/', views.ajouter_categorie, name='ajouter_categorie'),
    path('categories/modifier/<int:categorie_id>/', views.modifier_categorie, name='modifier_categorie'),
    path('categories/supprimer/<int:categorie_id>/', views.supprimer_categorie),
    path('categories/', views.liste_categories, name='liste_categories'),
    path('categories/ajouter/', views.ajouter_categorie, name='ajouter_categorie'),
    path('categories/modifier/<int:categorie_id>/', views.modifier_categorie, name='modifier_categorie'),
    path('categories/supprimer/<int:categorie_id>/', views.supprimer_categorie, name='supprimer_categorie'),


]