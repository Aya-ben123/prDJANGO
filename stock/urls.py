from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    # Page d'accueil
    path('', views.home, name='home'),
    
    # Page de connexion
    path('login/', views.login_view, name='login'),
    
    # Liste des produits
    path('produits/', views.produit_list, name='produit_list'),
    
    # Ajouter un produit
    path('ajouter/', views.produit_create, name='produit_create'),
    
    # Modifier un produit (en utilisant l'identifiant)
    path('<int:pk>/modifier/', views.produit_update, name='produit_update'),
    
    # Supprimer un produit (en utilisant l'identifiant)
    path('<int:pk>/supprimer/', views.produit_delete, name='produit_delete'),
]

# Serve les fichiers média (images de produits) pendant le développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
