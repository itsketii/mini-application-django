from django.urls import path
from . import views

app_name = 'iit_underground'

urlpatterns = [
    path('', views.fil_actualite, name='fil'),
    path('inscription/', views.inscription, name='inscription'),
    path('nouveau/', views.creer_post, name='creer'),
    path('profil/', views.profil_utilisateur, name='profil'),
    path('profil/supprimer/', views.supprimer_compte, name='supprimer_compte'),
    path('commentaire/<int:commentaire_id>/supprimer/', views.supprimer_commentaire, name='supprimer_commentaire'),
    path('<int:post_id>/modifier/', views.modifier_post, name='modifier'),
    path('<int:post_id>/supprimer/', views.supprimer_post, name='supprimer'),
    path('<int:post_id>/', views.detail_post, name='detail'),
]