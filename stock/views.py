from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProduitForm
from .models import Product
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Page d'accueil
def home(request):
    return render(request, 'stock/home.html') 

# Affichage des produits
def produit_list(request):
    query = request.GET.get('q')
    if query:
        produits = Product.objects.filter(name__icontains=query)  # Remplacer 'nom' par 'name'
    else:
        produits = Product.objects.all()
    return render(request, 'stock/produit_list.html', {'produits': produits})

# Page de connexion
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authentification de l'utilisateur
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('produit_list')  # Redirection vers la liste après login
        else:
            messages.error(request, 'Nom d’utilisateur ou mot de passe incorrect.')
    
    return render(request, 'stock/login.html')

# Ajouter un produit
def produit_create(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Produit ajouté avec succès.")
            return redirect('produit_list')
    else:
        form = ProduitForm()

    return render(request, 'stock/produit_form.html', {'form': form})

# Modifier un produit
def produit_update(request, pk):
    produit = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProduitForm(request.POST, request.FILES, instance=produit)
        if form.is_valid():
            form.save()
            return redirect('produit_list')
    else:
        form = ProduitForm(instance=produit)
    
    return render(request, 'stock/produit_form.html', {'form': form})


# Supprimer un produit
def produit_delete(request, pk):
    produit = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        produit.delete()
        messages.success(request, "Produit supprimé avec succès.")
        return redirect('produit_list')
    return render(request, 'stock/produit_confirm_delete.html', {'produit': produit})
