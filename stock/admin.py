from django.contrib import admin
from .models import Category, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'quantity')  # Ajouter 'quantity' à la liste des champs affichés
    list_filter = ('category',)  # Facultatif : Permet de filtrer par catégorie
    search_fields = ('name',)  # Facultatif : Permet de rechercher par nom du produit
    ordering = ('name',)  # Facultatif : Trie par défaut par le nom

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)



