from django.urls import path
from . import views

app_name = 'iit_underground'

urlpatterns = [
    path('', views.fil_actualit    git add iit_underground/urls.pye, name='fil'),
    path('inscription/', views.inscription, name='inscription'),
    path('nouveau/', views.creer_potin, name='creer'),
    path('profil/', view.profil_utlisateur, name='profil'),
    path('<int:potin_id>/modifier/', views.modifier_potin, name='modifier'),
    path('<int:potin_id>/supprimer/', views.supprimer_potin, name='supprimer'),
    path('<int:potin_id>/', views.detail_potin, name='detail'),
]