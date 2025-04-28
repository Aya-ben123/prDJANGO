from django.db import models

# Modèle pour les catégories de produits
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Modèle pour les produits
class Product(models.Model):
    name = models.CharField(max_length=200)  # Nom du produit
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Prix du produit
    description = models.TextField()  # Description du produit
    image = models.ImageField(upload_to='products/', blank=True, null=True)  # Image du produit (facultatif)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')  # Catégorie associée
    quantity = models.PositiveIntegerField(default=0)  # Ajouter le champ quantité

    def __str__(self):
        return self.name



