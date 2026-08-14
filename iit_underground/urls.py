from django.urls import path
from . import views


app_name = 'iit_underground'

urlpatterns = [
    path('', views.fil_actualite, name='fil'),
    path('inscription/', views.inscription, name='inscription'),
    path('nouveau/', views.creer_potin, name='creer'),
    path('<int:pk>/modifier/', views.modifier_potin, name='modifier'),
    path('<int:pk>/supprimer/', views.supprimer_potin, name='supprimer'),
    path('<int:potin_id>/', views.detail_potin, name='detail')
]