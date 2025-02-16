from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom

class Produit(models.Model):
    nom = models.CharField(max_length=255)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.nom

class Vente(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()
    prix_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date_vente = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.prix_total = self.produit.prix * self.quantite
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Vente de {self.quantite} {self.produit.nom} le {self.date_vente}"
