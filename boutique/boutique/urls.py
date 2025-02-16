
from django.contrib import admin
from django.urls import path, include
from gestion.views import accueil  # Import de la fonction accueil

urlpatterns = [
    path('', accueil, name='accueil'),  # Affiche la page d'accueil
    path('admin/', admin.site.urls),
    path('produits/', include('gestion.urls')),
]
